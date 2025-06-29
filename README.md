# CarSal – Used-Car Marketplace (Flask + Bootstrap)

A next-generation platform that uncovers *hidden-gem* vehicles—clean, rebuilt, or salvage titles with years of life left—so everyday buyers can save thousands without the guess-work.  
Built with **Flask + Jinja2 + Bootstrap 5**, fully responsive, and easily deployable on any WSGI-compatible host.

---

## Development Timeline (2025-06-18 → present)

| Phase | Key Tasks | Output / Highlights |
|-------|-----------|---------------------|
| **1 · Foundation** | • Chose Flask + Jinja2 + Bootstrap<br>• Created `app.py / templates / static` skeleton<br>• CSV ingest → vehicle cards + prototype recommender | Conda + VS Code ready<br>Hot-reload Flask server |
| **2 · Core Pages** | Built `index.html`, `listing.html`, `car_detail.html`, `favorites.html`, `recommend.html` | Dynamic images, clean `url_for` loops |
| **3 · Visual / UX** | Hero carousel, “How It Works” icons, testimonials, FAQ accordion, donation & CTA bands | Brand palette `#EF8B3B / #313F81 / #FFFFFF`<br>Plus Jakarta Sans site-wide |
| **4 · Site Template** | `base.html` with sticky navbar, mega-menu, footer, flash messages | Logo sizing, button alignment, mega-menu click/scroll auto-close |
| **5 · Responsive & Motion** | Partner-logo marquee, social-icon blue-ring hover, P3 + sRGB colour validation | Fixed icon squash and hover tail |
| **6 · Rebrand** (AutoSeek → CarSal) | Copied repo, cleaned `.git` remotes, updated logo & copy, removed nonprofit badge | New GitHub repo **CarSal** live |
| **7 · About Page** | Added `about.html` with hero, mission, initiatives, impact, timeline, team, CTA | PNG team photos & initiative icons |
| **8 · Bug & UX Polish** | 404 / `url_for` fixes, image-path sanitiser, mega-menu overscroll patch | Smooth close on drag/bounce |
| **9 · Version / Deploy** | Cleaned `.git/config`, updated README, ensured multi-repo detection in GitHub Desktop | Histories of AutoSeek and CarSal separated |

---

## Project Structure

```text
CarSal/
├── app.py
├── used_cars.csv
├── static/
│   ├── car_images/
│   ├── images/          # hero / banners
│   ├── icons/
│   │   ├── logo.png
│   │   └── initiatives/
│   └── partners/        # partner logos
└── templates/
    ├── base.html
    ├── index.html
    ├── listing.html
    ├── car_detail.html
    ├── favorites.html
    ├── recommend.html
    └── about.html
```

---

## Quick Start

```bash
# clone repo & enter
git clone https://github.com/<your-org>/CarSal.git
cd CarSal

# create & activate environment
conda create -n carsal python=3.11 pandas flask
conda activate carsal

# run development server
python app.py
# open http://127.0.0.1:5000
```

---

## Roadmap

* Search and server-side pagination  
* Contact / Careers pages with form handling  
* Recommendation v2 — cosine similarity plus price weighting  
* Image CDN and thumbnail generation  
* Dockerfile + GitHub Actions for automatic deploy

---

## License

MIT — fork, extend, and build your own car-marketplace variant.