from django.conf import settings
from django.http import JsonResponse

class BlockedIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_ips = settings.BLOCKED_IPS  # Engellenmiş IP adreslerini ayarlardan alıyoruz
        ip = request.META.get('REMOTE_ADDR')  # Gelen isteğin IP adresini alıyoruz
        if ip in blocked_ips:  # Eğer gelen IP engellenmişse
            return JsonResponse({'detail': 'IP address is blocked'}, status=403)
        
        response = self.get_response(request)  # Eğer engellenmemişse, isteği geçmesine izin veriyoruz
        return response
