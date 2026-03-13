"""Lazy resource initialisation using Managed Identity (DefaultAzureCredential)."""
import os, logging
from azure.identity import DefaultAzureCredential

log = logging.getLogger(__name__)
_credential = None

def get_credential():
    global _credential
    if _credential is None:
        _credential = DefaultAzureCredential()
    return _credential
