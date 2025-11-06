"""
config.py - 설정 파일

주의: 이 파일은 현재 app.py에서 사용되지 않습니다.
필요하지 않다면 삭제해도 됩니다.
"""
import streamlit as st
from anthropic import Anthropic

# Anthropic API 설정
anthropic_api_key = st.secrets.get("ANTHROPIC_API_KEY", "")
anthropic = Anthropic(api_key=anthropic_api_key)