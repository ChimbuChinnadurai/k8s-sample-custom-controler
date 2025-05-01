# k8s-sample-custom-controler

# Command to generate cert for webhooks

```
openssl req -x509 -sha256 -newkey rsa:2048 -keyout tls.key -out tls.crt -days 1024 -nodes -addext "subjectAltName = DNS.1:validate.validate.svc"
```

base64 encode the key and cert file and save as a kubernetes secret for the application. Base64 encode the cert file and add that in webhook caBundle

# sample kubernetes command to create the secret
```
 kubectl create secret tls admission-tls --cert tls.crt --key tls.key --namespace validate
```

# Docker commands

```
docker buildx build -f Dockerfile --platform linux/amd64 --tag simbu1290/k8s:validating-webhook-v1 --no-cache .
docker push simbu1290/k8s:validating-webhook-v1
```