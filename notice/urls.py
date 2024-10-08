from notice.apps import NoticeConfig
from notice.views import (
    AdsCreateAPIView,
    AdsDestroyAPIView,
    AdsListAPIView,
    AdsRetrieveAPIView,
    AdsUpdateAPIView,
    ReviewCreateAPIView,
    ReviewDestroyAPIView,
    ReviewListAPIView,
    ReviewUpdateAPIView,
)
from django.urls import path

app_name = NoticeConfig.name

urlpatterns = [
    path("", AdsListAPIView.as_view(), name="ad_list"),
    path("<int:pk>/", AdsRetrieveAPIView.as_view(), name="ad_detail"),
    path("create/", AdsCreateAPIView.as_view(), name="ad_create"),
    path("update/<int:pk>/", AdsUpdateAPIView.as_view(), name="ad_change"),
    path("delete/<int:pk>/", AdsDestroyAPIView.as_view(), name="ad_delete"),
    path("<int:ad_id>/review/", ReviewListAPIView.as_view(), name="review_list"),
    path(
        "<int:ad_id>/review/create/",
        ReviewCreateAPIView.as_view(),
        name="review_create",
    ),
    path(
        "<int:ad_id>/review/update/<int:pk>/",
        ReviewUpdateAPIView.as_view(),
        name="review_change",
    ),
    path(
        "<int:ad_id>/review/delete/<int:pk>/",
        ReviewDestroyAPIView.as_view(),
        name="review_delete",
    ),
]
