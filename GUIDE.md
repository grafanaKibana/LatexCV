# Complete Guide to LatexCV Repository

## Overview

This repository contains a LaTeX-based CV/Resume system using the **Awesome CV** template. It generates three types of documents:
- **CV (Curriculum Vitae)** - Comprehensive academic/professional document
- **Resume** - Concise professional summary
- **Cover Letter** - Job application letter

All documents are compiled from modular LaTeX files into PDFs using XeLaTeX.

---

## Repository Structure

```
LatexCV/
├── awesome-cv.cls              # Main LaTeX class file (template engine)
├── Makefile                    # Build automation
├── compiled/                   # Output directory for PDFs
├── latex/
│   ├── awesome-cv.cls          # Copy of class file (for latex/ subdirectory)
│   ├── profile.png             # Profile photo
│   ├── cv/                     # CV-specific sections
│   │   ├── cv.tex              # Main CV document
│   │   ├── education.tex
│   │   ├── experience.tex
│   │   ├── skills.tex
│   │   ├── honors.tex
│   │   ├── certificates.tex
│   │   ├── presentation.tex
│   │   ├── writing.tex
│   │   └── committees.tex
│   ├── resume/                 # Resume-specific sections
│   │   ├── resume.tex          # Main Resume document
│   │   ├── summary.tex
│   │   ├── education.tex
│   │   ├── experience.tex
│   │   ├── honors.tex
│   │   ├── certificates.tex
│   │   └── ... (other sections)
│   └── coverletter/
│       └── coverletter.tex     # Cover letter document
```

---

## How It Works

### 1. **Class File (`awesome-cv.cls`)**
The heart of the system. This LaTeX class file defines:
- Document layout and formatting
- Custom commands (`\cventry`, `\cvsection`, `\cvskill`, etc.)
- Color schemes and typography
- Header/footer structures
- Personal information commands (`\name`, `\email`, `\github`, etc.)

**You typically don't need to modify this file** unless you want to change fundamental styling.

### 2. **Main Documents**
Each document type has a main `.tex` file:
- `latex/cv/cv.tex` - CV document
- `latex/resume/resume.tex` - Resume document  
- `latex/coverletter/coverletter.tex` - Cover letter

These files:
- Set up the document class
- Configure personal information
- Import section files using `\input{...}`
- Generate the final PDF

### 3. **Section Files**
Content is organized into separate `.tex` files for each section:
- Each section file uses commands like `\cvsection{Title}` and `\cventry{...}`
- Sections can be easily enabled/disabled by commenting out `\input{...}` lines
- Content is modular and reusable

### 4. **Build System (`Makefile`)**
The Makefile automates compilation:
- Finds all `.tex` files in each directory
- Compiles using `xelatex`
- Outputs PDFs to `compiled/` directory

---

## Prerequisites

### Required Software
1. **TeX Distribution**: 
   - **TeX Live** (recommended) - [Installation guide](https://www.tug.org/texlive/)
   - Or use Docker (see below)

2. **XeLaTeX**: Included with TeX Live
   - Required for Unicode support and custom fonts

### Installation Options

**Option 1: Local Installation (macOS)**
```bash
# Using Homebrew
brew install --cask mactex

# Or install BasicTeX (smaller)
brew install --cask basictex
# Then install additional packages:
sudo tlmgr update --self
sudo tlmgr install fontawesome6 roboto sourcesanspro
```

**Option 2: Docker (No Local Installation)**
```bash
docker run --rm --user $(id -u):$(id -g) -i -w "/doc" \
  -v "$PWD":/doc texlive/texlive:latest make
```

---

## Building Documents

### Using Make (Recommended)

**Build all documents:**
```bash
make
```

**Build specific document:**
```bash
make resume.pdf
make cv.pdf
make coverletter.pdf
```

**Clean compiled PDFs:**
```bash
make clean
```

### Manual Compilation

If you prefer to compile manually:

```bash
# For CV
xelatex -output-directory=compiled latex/cv/cv.tex

# For Resume
xelatex -output-directory=compiled latex/resume/resume.tex

# For Cover Letter
xelatex -output-directory=compiled latex/coverletter/coverletter.tex
```

**Note**: You may need to run `xelatex` twice to resolve cross-references properly.

---

## Making Changes

### 1. **Update Personal Information**

Edit the main document files:
- `latex/cv/cv.tex` (lines 48-79)
- `latex/resume/resume.tex` (lines 48-79)
- `latex/coverletter/coverletter.tex` (lines 48-99)

**Available commands:**
```latex
\name{First}{Last}                    % Your name
\position{Job Title}                   % Current position
\address{Your Address}                 % Physical address
\mobile{+1-234-567-8900}             % Phone number
\email{your.email@example.com}         % Email address
\homepage{www.yoursite.com}           % Personal website
\github{yourusername}                  % GitHub username
\linkedin{yourusername}                % LinkedIn username
\photo[circle,edge,left]{latex/profile.png}  % Profile photo
\quote{"Your quote here"}              % Personal quote
```

**Social Media Options:**
- `\github{username}`
- `\linkedin{username}`
- `\twitter{handle}`
- `\gitlab{username}`
- `\stackoverflow{id}{name}`
- `\googlescholar{id}{name}`
- `\orcid{id}`
- `\medium{username}`
- `\kaggle{handle}`
- And many more...

### 2. **Modify Section Content**

#### **Experience Section** (`latex/shared/experience.tex`)

**Structure:**
```latex
\cvsection{Experience}

\begin{cventries}
  \cventry
    {Job Title}                    % Position
    {Company Name}                 % Organization
    {Location}                     % Location
    {Date Range}                   % Date(s)
    {
      \begin{cvitems}
        \item {First accomplishment or responsibility}
        \item {Second accomplishment or responsibility}
        \item {Third accomplishment or responsibility}
      \end{cvitems}
    }
\end{cventries}
```

**Example:**
```latex
\cventry
  {Senior Software Engineer}
  {Tech Company Inc.}
  {San Francisco, CA}
  {Jan. 2020 - Present}
  {
    \begin{cvitems}
      \item {Led development of microservices architecture}
      \item {Reduced system latency by 40\%}
      \item {Mentored team of 5 junior engineers}
    \end{cvitems}
  }
```

#### **Education Section** (`latex/shared/education.tex`)

**Structure:**
```latex
\cvsection{Education}

\begin{cventries}
  \cventry
    {Degree}                       % Degree
    {Institution Name}             % Institution
    {Location}                     % Location
    {Date Range}                   % Date(s)
    {
      \begin{cvitems}
        \item {Honor, award, or notable achievement}
      \end{cvitems}
    }
\end{cventries}
```

#### **Skills Section** (`latex/shared/skills.tex`)

**Structure:**
```latex
\cvsection{Skills}

\begin{cvskills}
  \cvskill
    {Category}                     % Skill category
    {Skill1, Skill2, Skill3}       % Comma-separated skills
\end{cvskills}
```

**Example:**
```latex
\cvskill
  {Programming}
  {Python, JavaScript, Go, Rust}

\cvskill
  {Frameworks}
  {React, Django, FastAPI, TensorFlow}
```

#### **Summary Section** (Resume only: `latex/resume/summary.tex`)

**Structure:**
```latex
\cvsection{Summary}

\begin{cvparagraph}
Your professional summary paragraph here. This should be 2-3 sentences 
highlighting your key qualifications and experience.
\end{cvparagraph}
```

#### **Other Sections**

Similar patterns for:
- **Honors** (`latex/shared/honors.tex`) - Uses `\cvhonor{position}{title}{location}{date}`
- **Certificates** (`latex/shared/certificates.tex`) - Uses `\cventry`
- **Writing** (`latex/shared/writing.tex`) - Publications, articles
- **Presentations** (`latex/shared/presentation.tex`) - Conference talks
- **Committees** (`latex/shared/committees.tex`) - Professional service

### 3. **Enable/Disable Sections**

In the main document files (`cv.tex`, `resume.tex`), comment out sections you don't want:

```latex
% Comment out to disable a section
% \input{latex/shared/writing.tex}
% \input{latex/shared/committees.tex}
```

### 4. **Customize Colors**

In `latex/shared/config.tex`, modify the color scheme:

```latex
% Change highlight color
\colorlet{awesome}{awesome-blue}  % Options: awesome-red, awesome-blue, 
                                   % awesome-emerald, awesome-orange, etc.

% Or define custom color
\definecolor{awesome}{HTML}{CA63A8}  % Custom hex color
```

**Available predefined colors:**
- `awesome-red` (default)
- `awesome-emerald`
- `awesome-skyblue`
- `awesome-pink`
- `awesome-orange`
- `awesome-nephritis`
- `awesome-concrete`
- `awesome-darknight`

### 5. **Adjust Page Layout**

Modify margins in `latex/shared/config.tex`:

```latex
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}
```

### 6. **Change Font Size**

In the main document files:

```latex
\documentclass[11pt, a4paper]{awesome-cv}  % Change 11pt to 10pt or 12pt
```

### 7. **Header Alignment**

Control header alignment:

```latex
\makecvheader[C]  % C = center, L = left, R = right
```

### 8. **Footer Content**

Modify footer in main documents:

```latex
\makecvfooter
  {\today}                              % Left: Date
  {Your Name~~~·~~~Document Type}       % Center: Title
  {\thepage}                            % Right: Page number
```

---

## Cover Letter Customization

Edit `latex/coverletter/coverletter.tex`:

### Recipient Information
```latex
\recipient
  {Recipient Name}
  {Company Name\\Street Address\\City, State ZIP}
```

### Letter Content
```latex
\letterdate{\today}
\lettertitle{Job Application for Position Title}
\letteropening{Dear Hiring Manager,}
\letterclosing{Sincerely,}
\letterenclosure[Attached]{Resume}
```

### Letter Sections
```latex
\begin{cvletter}
\lettersection{Section Title}
Your paragraph content here.

\lettersection{Another Section}
More content here.
\end{cvletter}
```

---

## Common Customization Tasks

### Task 1: Add a New Experience Entry

1. Open `latex/shared/experience.tex`
2. Add a new `\cventry` block before `\end{cventries}`
3. Fill in the 5 parameters: position, company, location, dates, description
4. Compile: `make cv.pdf` or `make resume.pdf`

### Task 2: Update Skills

1. Open `latex/shared/skills.tex`
2. Modify existing `\cvskill` entries or add new ones
3. Compile

### Task 3: Change Color Scheme

1. Open `latex/cv/cv.tex` (or `latex/resume/resume.tex`)
2. Find line: `\colorlet{awesome}{awesome-red}`
3. Change to desired color: `\colorlet{awesome}{awesome-blue}`
4. Compile

### Task 4: Add Profile Photo

1. Place your photo in `latex/` directory (e.g., `latex/profile.png`)
2. In main document, uncomment/modify:
   ```latex
   \photo[circle,edge,left]{latex/profile.png}
   ```
   Options: `circle|rectangle`, `edge|noedge`, `left|right`
3. Compile

### Task 5: Create Resume from CV

1. Edit `latex/resume/resume.tex` to include only desired sections from `latex/shared/`
2. Add summary section (resume-specific)
3. Compile: `make resume.pdf`

---

## Troubleshooting

### Issue: "Font not found" errors

**Solution:** Install required fonts:
```bash
sudo tlmgr install fontawesome6 roboto sourcesanspro
```

### Issue: PDF not updating after changes

**Solution:** 
1. Run `make clean` to remove old PDFs
2. Recompile: `make`

### Issue: Compilation errors

**Common causes:**
- Missing closing braces `}`
- Unmatched `\begin{...}` and `\end{...}`
- Special characters not escaped (use `\&` instead of `&`, `\%` instead of `%`)

**Solution:** Check LaTeX syntax carefully, especially in section files.

### Issue: Section not appearing

**Solution:** 
1. Verify `\input{latex/cv/section.tex}` is not commented out
2. Check that section file exists
3. Ensure section file has proper `\cvsection{...}` command

---

## Best Practices

1. **Version Control**: Keep all `.tex` files in git, but ignore `compiled/` directory
2. **Modular Updates**: Update section files individually rather than editing main documents
3. **Consistent Formatting**: Use consistent date formats (e.g., "Jan. 2020 - Present")
4. **Regular Compilation**: Compile frequently to catch errors early
5. **Backup**: Keep backups of working versions before major changes
6. **Content Organization**: Keep related content together in section files

---

## Advanced Customization

### Modify Class File (Advanced)

If you need to change fundamental styling, edit `awesome-cv.cls`:
- Font sizes: Lines 177-220
- Colors: Lines 124-151
- Layout: Lines 106-108 (margins)
- Section styles: Lines 184-220

**Warning**: Changes to the class file affect all documents. Test thoroughly.

### Custom Commands

You can define custom commands in section files:

```latex
% Define a custom command
\newcommand{\mycustomtext}[1]{\textbf{#1}}

% Use it
\mycustomtext{Important text}
```

---

## Quick Reference

### Essential Commands

| Command | Usage | Example |
|---------|-------|---------|
| `\cvsection{Title}` | Section heading | `\cvsection{Experience}` |
| `\cventry{pos}{org}{loc}{date}{desc}` | Experience/Education entry | See examples above |
| `\cvskill{cat}{skills}` | Skills entry | `\cvskill{DevOps}{AWS, Docker}` |
| `\cvhonor{pos}{title}{loc}{date}` | Honor/Award entry | `\cvhonor{1st Place}{Competition}{City}{2020}` |
| `\begin{cvitems}...\end{cvitems}` | Bullet list | Inside `\cventry` descriptions |
| `\begin{cvparagraph}...\end{cvparagraph}` | Paragraph text | For summary sections |

### File Locations

| Document | Main File | Sections Directory |
|----------|-----------|-------------------|
| CV | `latex/cv/cv.tex` | `latex/cv/` |
| Resume | `latex/resume/resume.tex` | `latex/resume/` |
| Cover Letter | `latex/coverletter/coverletter.tex` | N/A |

---

## Summary

This repository provides a professional, modular LaTeX-based CV system. Key points:

1. **Structure**: Main documents import modular section files
2. **Build**: Use `make` to compile all documents
3. **Customization**: Edit section files for content, main files for personal info/styling
4. **Output**: PDFs generated in `compiled/` directory
5. **Flexibility**: Easy to enable/disable sections and customize appearance

Start by updating personal information in the main document files, then modify section content as needed. Compile frequently to see your changes!
