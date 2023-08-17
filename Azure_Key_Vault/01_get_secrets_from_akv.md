# 1.Install keyvault library


```python
pip3 install azure-identity azure-keyvault-secrets
```

# 2.Create Secret client


```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Azure Key Vault URL
key_vault_url = "https://akv.vault.azure.net/"

# Create a DefaultAzureCredential object for authentication
credential = DefaultAzureCredential()

# Create a SecretClient using the DefaultAzureCredential
secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

```

# 3.Retrieve a secret from Key Vault


```python

secret_name = "storage-key"
secret = secret_client.get_secret(secret_name)

# Extract the secret value
secret_value = secret.value
```
