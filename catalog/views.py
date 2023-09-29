from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpRequest,
    HttpResponse, HttpResponseRedirect,
)
from django.urls import reverse_lazy
from django.views import generic

from .models import (
    Clothing,
    Designer,
    Size,
    Material,
    ClothingType,
)
from .forms import (
    ByNameSearchForm,
    SizeForm,
    DesignerSearchForm,
    DesignerCreationForm,
    DesignerUpdateForm,
    ClothingForm,
)


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_clothes = Clothing.objects.all().count()
    num_designers = Designer.objects.all().count()
    num_clothing_types = ClothingType.objects.all().count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    contex = {
        "num_clothes": num_clothes,
        "num_designers": num_designers,
        "num_clothing_types": num_clothing_types,
        "num_visits": num_visits + 1,
    }
    return render(request, "catalog/index.html", context=contex)


class ClothingTypeListView(LoginRequiredMixin, generic.ListView):
    model = ClothingType
    context_object_name = "clothing_type_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(ClothingTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_from"] = ByNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> ClothingType:
        form = ByNameSearchForm(self.request.GET)
        queryset = ClothingType.objects.all()
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class ClothingTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = ClothingType
    fields = "__all__"
    success_url = reverse_lazy("catalog:clothing-type-list")


class ClothingTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = ClothingType
    fields = "__all__"
    success_url = reverse_lazy("catalog:clothing-type-list")


class ClothingTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = ClothingType
    success_url = reverse_lazy("catalog:clothing-type-list")


class MaterialListView(LoginRequiredMixin, generic.ListView):
    model = Material
    context_object_name = "material_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(MaterialListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_from"] = ByNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> Material:
        form = ByNameSearchForm(self.request.GET)
        queryset = Material.objects.all()
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class MaterialCreateView(LoginRequiredMixin, generic.CreateView):
    model = Material
    fields = "__all__"
    success_url = reverse_lazy("catalog:material-list")


class MaterialUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Material
    fields = "__all__"
    success_url = reverse_lazy("catalog:material-list")


class MaterialDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Material
    success_url = reverse_lazy("catalog:material-list")


class SizeListView(LoginRequiredMixin, generic.ListView):
    model = Size
    context_object_name = "size_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(SizeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_from"] = ByNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> Size:
        form = ByNameSearchForm(self.request.GET)
        queryset = Size.objects.all()
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class SizeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Size
    form_class = SizeForm
    success_url = reverse_lazy("catalog:size-list")


class SizeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Size
    form_class = SizeForm
    success_url = reverse_lazy("catalog:size-list")


class SizeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Size
    success_url = reverse_lazy("catalog:size-list")


class DesignerListView(LoginRequiredMixin, generic.ListView):
    model = Designer
    queryset = Designer.objects.prefetch_related("clothes")
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(DesignerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["username"] = username
        context["search_from"] = DesignerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self) -> Designer:
        queryset = Designer.objects.all()
        form = DesignerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class DesignerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Designer


class DesignerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Designer
    form_class = DesignerCreationForm


class DesignerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Designer
    form_class = DesignerUpdateForm
    success_url = reverse_lazy("catalog:designer-list")


class DesignerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Designer
    success_url = reverse_lazy("")


class ClothingListView(LoginRequiredMixin, generic.ListView):
    model = Clothing
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(ClothingListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_from"] = ByNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> Clothing:
        queryset = Clothing.objects.all().select_related("clothing_type").prefetch_related("materials", "size", "designer")
        form = ByNameSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class ClothingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Clothing


class ClothingCreateView(LoginRequiredMixin, generic.CreateView):
    model = Clothing
    form_class = ClothingForm
    success_url = reverse_lazy("catalog:clothing-list")


class ClothingUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Clothing
    form_class = ClothingForm
    success_url = reverse_lazy("catalog:clothing-list")


class ClothingDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Clothing
    success_url = reverse_lazy("catalog:clothing-list")


@login_required
def toggle_assign_to_clothing(request, pk) -> HttpResponseRedirect:
    designer = Designer.objects.get(id=request.user.id)
    if (
        Clothing.objects.get(id=pk) in designer.clothes.all()
    ):
        designer.clothes.remove(pk)
    else:
        designer.clothes.add(pk)
    return HttpResponseRedirect(reverse_lazy("catalog:clothing-detail", args=[pk]))

