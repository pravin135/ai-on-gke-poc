FROM ollama/ollama

# start ollama server temporarily and pull model
RUN ollama serve & \
    sleep 5 && \
    ollama pull tinyllama

EXPOSE 11434

CMD ["ollama", "serve"]
