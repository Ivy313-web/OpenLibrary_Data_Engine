# OpenLibrary_Data_Engine

A high-performance Python scraper using Requests and XPath (lxml) to extract multi-dimensional book data. Optimized for speed and structured data cleaning.

After building my BBC Scraper with Selenium, I wanted to explore **performance optimization**. By using `Requests` and `XPath`, this engine retrieves data significantly faster than traditional browser automation, while handling more complex data structures.

*****************************************************************************************************************************************************************************

Key Features
- **High-Speed Parsing**: Utilizes `lxml` and `XPath` for near-instant data extraction.
- **Deep Data Mining**: Scrapes Title, Author, User Ratings, "Want to Read" counts, and direct links.
- **Advanced Data Cleaning**: Custom logic to sanitize raw web text (removing noise, extra spaces, and newlines) for a professional output.
- **Multi-Format Storage**: Integrated module to export results into structured Excel (.xlsx) or CSV files.

Tech Stack
- **Networking**: `Requests` (handling HTTP/1.1)
- **Parsing Engine**: `lxml` / `XPath` (efficient DOM navigation)
- **Data Export**: `Openpyxl`, `CSV`, `OS`
- **Language**: Python 3.8+

Future Roadmap
- Implement **Multi-threading** to scrape 50+ pages in seconds.
- Add **Book Cover Downloader** using `urllib`.
- Develop a **GUI (Graphical User Interface)** for non-technical users.
  
***********************************************************************************
How to run?                                          
In the side document panel：
library.py(main file)
library_save_method.py(save method file)

OR

clone the addresss:https://github.com/Ivy313-web/OpenLibrary_Data_Engine.git
***********************************************************************************

New code, new knowledge, isn't it?😎

