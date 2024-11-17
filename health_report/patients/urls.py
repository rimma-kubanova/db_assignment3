from rest_framework.routers import DefaultRouter
from .views import (
    UsersViewSet, PatientsViewSet, DiseaseTypeViewSet, CountryViewSet, DiseaseViewSet,
    DiscoverViewSet, PatientDiseaseViewSet, PublicServantViewSet, DoctorViewSet,
    SpecializeViewSet, RecordViewSet
)

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register('patients', PatientsViewSet)
router.register('diseasetypes', DiseaseTypeViewSet)
router.register('countries', CountryViewSet)
router.register('diseases', DiseaseViewSet)
router.register('discover', DiscoverViewSet)
router.register('patientdiseases', PatientDiseaseViewSet)
router.register('publicservants', PublicServantViewSet)
router.register('doctors', DoctorViewSet)
router.register('specialize', SpecializeViewSet)
router.register(r'records', RecordViewSet)

urlpatterns = router.urls