from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from annotator import views

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('schema/', schema_view, name='schema'),
    #path('annotator/', views.snippet_list),
    path('annotator/', views.api_root),
    path('annotator/model/', views.ModelList.as_view(), name='model-list'),
    path('annotator/model/<int:pk>/', views.ModelDetail.as_view(), name='model-detail'),
    path('annotator/model/<int:pk>/train/', views.trainModel, name='model-train'),
    path('annotator/model/<int:mk>/annotate/<int:sk>/', views.annotate, name='model-annotate'),

    #path('annotator/model/findByTags/', views.model_list_by_tags),
    #path('annotator/model/findByStatus/', views.model_list_by_status),
    path('annotator/corpus/', views.CorpusList.as_view(), name='corpus-list'),
    path('annotator/corpus/<int:pk>/', views.CorpusDetail.as_view(), name='corpus-detail'),
    path('annotator/corpus/<int:pk>/segments/', views.SegmentsInCorpus.as_view(), name='corpussegment-list'),
    path('annotator/corpus/<int:pk>/addsegments/<str:s_list>/', views.addsegmentstocorpus, name='corpussegment-add'),
    path('annotator/corpus/<int:pk>/removesegments/<str:s_list>/', views.removesegmentsfromcorpus, name='corpussegment-remove'),

    path('annotator/segment/', views.SegmentList.as_view(), name='segment-list'),
    path('annotator/segment/<int:pk>/', views.SegmentDetail.as_view(), name='segment-detail'),
    path('annotator/segment/<int:pk>/annotations/', views.AnnotationsInSegment.as_view(), name='annotationsegment-detail'),
    path('annotator/segment/<int:pk>/addannotations/<str:s_list>/', views.addannotationstosegment, name='segmentannot-add'),
    path('annotator/segment/<int:pk>/removeannotations/<str:s_list>/', views.removeannotationsfromsegment, name='segmentannot-remove'),
    path('annotator/segment/<int:sk>/annotate/<int:mk>/', views.annotate, name='annotate'),
    path('annotator/annotation/', views.AnnotationList.as_view(), name='annotation-list'),
    path('annotator/annotation/<int:pk>/', views.AnnotationDetail.as_view(), name='annotation-detail'),
    path('annotator/textannotation/', views.TextAnnotationList.as_view(), name='textannotation-list'),
    path('annotator/textannotation/<int:pk>/', views.TextAnnotationDetail.as_view(), name='textannotation-detail'),
    path('annotator/audioannotation/', views.AudioAnnotationList.as_view(), name='audioannotation-list'),
    path('annotator/audioannotation/<int:pk>/', views.AudioAnnotationDetail.as_view(), name='audioannotation-detail'),
    path('annotator/spantextannotation/', views.SpanTextAnnotationList.as_view(), name='spantextannotation-list'),
    path('annotator/spantextannotation/<int:pk>/', views.SpanTextAnnotationDetail.as_view(), name='spantextannotation-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    

]

urlpatterns = format_suffix_patterns(urlpatterns)
