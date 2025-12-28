.PHONY: compiled

CC = xelatex
OUTPUT_DIR = compiled
RESUME_DIR = latex/resume
CV_DIR = latex/cv
COVERLETTER_DIR = latex/coverletter
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
CV_SRCS = $(shell find $(CV_DIR) -name '*.tex')
COVERLETTER_SRCS = $(shell find $(CV_DIR) -name '*.tex')

examples: $(foreach x, coverletter cv resume, $x.pdf)

resume.pdf: $(RESUME_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(OUTPUT_DIR) $<

cv.pdf: $(CV_DIR)/cv.tex $(CV_SRCS)
	$(CC) -output-directory=$(OUTPUT_DIR) $<

coverletter.pdf: $(COVERLETTER_DIR)/coverletter.tex $(COVERLETTER_SRCS)
	$(CC) -output-directory=$(OUTPUT_DIR) $<

clean:
	rm -rf $(OUTPUT_DIR)/*.pdf
