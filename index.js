function removeEmptyHeaders(headers) {
  const newHeaders = new Headers();
  headers.forEach((value, key) => {
    if (!(value && value !== "undefined" && value !== "null")) {
        newHeaders.set(key, value);
    }
  });

  return newHeaders;
}
