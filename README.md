# 🌌 Orion Net — A Tiny Text‑Based Internet Protocol

Orion Net is a **minimal, human‑readable, text‑only internet protocol** built from scratch.  
No HTML. No JavaScript. No CSS. No ICANN. No DNS.  
Just simple documents, simple servers, and simple clients.

It’s inspired by the spirit of Gopher and Gemini — but lighter, smaller, and easier to implement.

Orion:// is powered by hopes, dreams, and Python.

---

## ✨ Features

- **Simple request format**  
  One line:  
  ```
  orion://host/path
  ```

- **Simple response format**  
  ```
  <status> <meta>\r\n
  <body>
  ```

- **OTXT content format**  
  A tiny, readable markup language:
  - `# Heading`
  - `* Lists`
  - `=> orion://link Label`
  - Code blocks  
  - Plain text

- **Reference server** (Python)  
- **Reference client** (Python)  
- **CLI browser** with link navigation, headings, lists, and code rendering  
- **Works offline, on LAN, or on the public internet**  
- **No ICANN or DNS required** — custom hostnames are free

---

## 🚀 Quick Start

### 1. Run the server

```
python orionsrv.py
```

You should see:

```
Orion Net server running on port 4040
```

### 2. Run the browser

```
python orionbrz.py orion://localhost/
```

---

## 📄 Demo

Here’s Orion Net serving a real OTXT page:

```
STATUS: 20 text/orion

──────────────── ORION PAGE ────────────────
HELLO ORION NET V0.1!!
• This proticol is light
• Easy

And it bloody well works!!

[1] about
────────────────────────────────────────────
Commands: number = follow link, b = back, q = quit
```

Following link `[1]`:

```
ABOUT

ORION:// Is an opensource web proticol that is powered by hopes, dreams and python.
```

This is the entire Orion experience — clean, readable, and fun.

---

## 📦 Repository Contents

This repo includes:

- `orionsrv.py` — Orion reference server  
- `orionrd.py` — Basic client  
- `orionbrz.py` — CLI browser  
- `pages/` — Example OTXT pages  

---

## 📚 OTXT Format (Orion Text)

OTXT is Orion’s native document format.

Examples:

### Heading
```
# Welcome to Orion
```

### List
```
* Fast
* Simple
* Text-only
```

### Link
```
=> orion://localhost/about About this server
```

### Code block
```
```
print("Hello Orion")
```
```

OTXT is intentionally tiny — easy to parse, easy to write.


## 🌍 Running Orion on the Internet

Orion does **not** require DNS or ICANN.

You can host Orion publicly by:

1. Port forwarding **4040 → your PC**  
2. Allowing port 4040 in Windows Firewall  
3. Running the server  
4. Sharing your public IP:

```
orion://YOUR_PUBLIC_IP/
```

Orion hostnames are free — you define them.

---

## 📝 License

MIT License (or whichever you choose)

---

## 💫 About

Orion Net is an experimental protocol created for fun, learning, and exploration.  
It’s tiny, friendly, and easy to hack on.

If you want a simpler web, Orion is for you.
 
