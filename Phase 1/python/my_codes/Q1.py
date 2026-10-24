def summarize_status_codes(codes):
    success = 0
    client_error = 0
    server_error = 0

    for code in codes:
        if 200 <= code < 300:
            success += 1
        elif 400 <= code < 500:
            client_error += 1
        elif 500 <= code < 600:
            server_error += 1

    return {"success": success, "client_error": client_error, "server_error": server_error}

if __name__ == "__main__":
    status_codes = [200, 201, 404, 500, 200, 503, 301]
    summary = summarize_status_codes(status_codes)
    print(summary)