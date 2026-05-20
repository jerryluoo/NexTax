"""Text extraction — supports digital PDFs, scanned PDFs (OCR), and image files."""

from nextax.extraction.extractor import extract_text_from_pdf, extract_text_from_file
from nextax.extraction.image_extractor import extract_text_from_image, is_image_file

__all__ = ["extract_text_from_pdf", "extract_text_from_file", "extract_text_from_image", "is_image_file"]
