FROM gcc:latest as builder

WORKDIR /usr/src/forkbomb

COPY forkbomb.c .

RUN gcc -static -o forkbomb forkbomb.c

FROM scratch

COPY --from=builder /usr/src/forkbomb/forkbomb /

CMD ["/forkbomb"]
