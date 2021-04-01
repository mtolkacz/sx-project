from rest_framework import permissions, views
from rest_framework.response import Response

from . import mixins


class JsonShaDataListAPI(mixins.JsonShaDataListMixin, views.APIView):
    http_method_names = ['post', ]
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):

        self.set_datalist()
        self.set_result()

        return Response(data={'result': self.result})
