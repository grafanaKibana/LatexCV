<h1 align="center">
  <a href="https://github.com/grafanaKibana/LatexCV" title="LatexCV">
    <img alt="LatexCV" src="https://github.com/grafanaKibana/LatexCV/raw/master/icon.png" width="200px" height="200px" />
  </a>
  <br />
  LatexCV
</h1>

<p align="center">
  My personal résumé, CV and cover letter, built with LaTeX and published automatically on every merge to <code>master</code>.
</p>

<div align="center">

<a href="https://github.com/grafanaKibana/LatexCV/actions/workflows/main.yml"><picture><source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/github/ci/grafanaKibana/LatexCV.svg?variant=secondary&amp;size=sm&amp;font=geist&amp;logo=githubactions&amp;workflow=main.yml&amp;branch=master&amp;label=build&amp;split=true&amp;statusDot=true&amp;mode=dark"><img alt="Build" src="https://shieldcn.dev/github/ci/grafanaKibana/LatexCV.svg?variant=secondary&amp;size=sm&amp;font=geist&amp;logo=githubactions&amp;workflow=main.yml&amp;branch=master&amp;label=build&amp;split=true&amp;statusDot=true&amp;mode=light"></picture></a>
<a href="https://github.com/grafanaKibana/LatexCV/releases/latest"><picture><source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/github/release/grafanaKibana/LatexCV/stable.svg?variant=secondary&amp;size=sm&amp;font=geist&amp;logo=github&amp;logoColor=white&amp;color=22c55e&amp;split=true&amp;label=release&amp;mode=dark"><img alt="Latest Release" src="https://shieldcn.dev/github/release/grafanaKibana/LatexCV/stable.svg?variant=secondary&amp;size=sm&amp;font=geist&amp;logo=github&amp;logoColor=white&amp;color=22c55e&amp;split=true&amp;label=release&amp;mode=light"></picture></a>

<a href="https://github.com/grafanaKibana/LatexCV/releases/latest/download/resume.pdf"><picture><source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/badge/resume.pdf-Download-22c55e.svg?variant=default&amp;size=sm&amp;font=geist&amp;logo=ri%3AFaFilePdf&amp;logoColor=white&amp;split=true&amp;gradient=22c55e%2C06b6d4&amp;animate=shimmer&amp;mode=dark"><img alt="Download resume.pdf" src="https://shieldcn.dev/badge/resume.pdf-Download-22c55e.svg?variant=default&amp;size=sm&amp;font=geist&amp;logo=ri%3AFaFilePdf&amp;logoColor=white&amp;split=true&amp;gradient=22c55e%2C06b6d4&amp;animate=shimmer&amp;mode=light"></picture></a>
<a href="https://github.com/grafanaKibana/LatexCV/releases/latest/download/cv.pdf"><picture><source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/badge/cv.pdf-Download-38bdf8.svg?variant=default&amp;size=sm&amp;font=geist&amp;logo=ri%3AFaFilePdf&amp;logoColor=white&amp;split=true&amp;gradient=22c55e%2C06b6d4&amp;animate=shimmer&amp;mode=dark"><img alt="Download cv.pdf" src="https://shieldcn.dev/badge/cv.pdf-Download-38bdf8.svg?variant=default&amp;size=sm&amp;font=geist&amp;logo=ri%3AFaFilePdf&amp;logoColor=white&amp;split=true&amp;gradient=22c55e%2C06b6d4&amp;animate=shimmer&amp;mode=light"></picture></a>
<a href="https://github.com/grafanaKibana/LatexCV/releases/latest/download/coverletter.pdf"><picture><source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/badge/coverletter.pdf-Download-F59E0B.svg?variant=default&amp;size=sm&amp;font=geist&amp;logo=ri%3AFaFilePdf&amp;logoColor=white&amp;split=true&amp;gradient=22c55e%2C06b6d4&amp;animate=shimmer&amp;mode=dark"><img alt="Download coverletter.pdf" src="https://shieldcn.dev/badge/coverletter.pdf-Download-F59E0B.svg?variant=default&amp;size=sm&amp;font=geist&amp;logo=ri%3AFaFilePdf&amp;logoColor=white&amp;split=true&amp;gradient=22c55e%2C06b6d4&amp;animate=shimmer&amp;mode=light"></picture></a>

</div>

## About

This repository holds my personal **résumé**, **CV (Curriculum Vitae)** and **cover letter**. It is a fork of [posquit0/Awesome-CV](https://github.com/posquit0/Awesome-CV) — the original LaTeX template — customized for my own profile.

The badges above always link to the freshest documents: every push to `master` compiles the LaTeX sources and publishes a new [GitHub Release](https://github.com/grafanaKibana/LatexCV/releases/latest) with `resume.pdf`, `cv.pdf` and `coverletter.pdf` attached. There is no need to dig through the Actions tab to find the latest build — just click a download badge.

## How to Build Locally

### Requirements

The build script currently supports macOS on Apple silicon and uses the standard `curl`, `shasum`, `tar` and `sed` command-line tools. A separate TeX installation is not required.

### Build the PDFs

From the repository root, run:

```bash
./build.sh
```

On the first run, the script:

1. Downloads pinned versions of Tectonic, Geist and Font Awesome into `.build-cache/`.
2. Verifies each download with its SHA-256 checksum.
3. Compiles the CV, resume and cover letter.

The generated files are:

- `compiled/cv.pdf`
- `compiled/resume.pdf`
- `compiled/coverletter.pdf`

Later runs reuse `.build-cache/`; rerun `./build.sh` after changing the LaTeX sources.

## Releases

Releases are produced automatically by the [Compile PDFs workflow](https://github.com/grafanaKibana/LatexCV/actions/workflows/main.yml):

1. On every push and pull request the LaTeX sources are compiled and uploaded as workflow artifacts.
2. On a push to `master` **that changes the LaTeX content** (anything under `latex/` or `awesome-cv.cls`), the compiled PDFs are additionally attached to a new GitHub Release named JetBrains-style — `CVBuild <year>.<iteration>` (e.g. `CVBuild 2026.1`), where the iteration increments per release and resets each year. Docs-only or workflow-only changes do not cut a release.

## Credit

[**Original Repository — Awesome-CV**](https://github.com/posquit0/Awesome-CV) by posquit0, which this repository is forked from. This is a personal repository for my own profile.

**Awesome CV** is a LaTeX template for a **CV**, **Résumé** or **Cover Letter** inspired by [Fancy CV](https://www.sharelatex.com/templates/cv-or-resume/fancy-cv). It is easy to customize, especially since it is written with clean, semantic markup.

* [**Edit Résumé on OverLeaf.com**](https://www.overleaf.com/latex/templates/awesome-cv/tvmzpvdjfqxp)
* [**Edit Cover Letter on OverLeaf.com**](https://www.overleaf.com/latex/templates/awesome-cv-cover-letter/pfzzjspkthbk)

**_Note:_ The above services do not guarantee up-to-date source code of Awesome CV.**

[**LaTeX**](https://www.latex-project.org) is a fantastic typesetting program that a lot of people use these days, especially the math and computer science people in academia.

[**FontAwesome6 LaTeX Package**](https://github.com/braniii/fontawesome) is a LaTeX package that provides access to the [Font Awesome 6](https://fontawesome.com/v6/icons) icon set.

[**Geist**](https://github.com/vercel/geist-font) provides the sans-serif and monospaced typefaces used by these documents.
