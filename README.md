# Case Study: Turning Messy Spreadsheets into a Usable Database

### **What This Method Achieves for Your Organisation**

This case study outlines a reliable, semi-automated process for turning chaotic legacy data into a pristine, structured, and strategic asset. Implementing this architectural pattern delivers direct, tangible benefits:

*   **Creates a single, trustworthy source of truth** by transforming scattered and inconsistent legacy data into a unified, reliable internal database.
*   **Frees up hundreds of hours of manual data cleaning** and reconciliation work, allowing your staff and volunteers to focus on high-value, mission-critical activities.
*   **Enables confident, evidence-based strategic planning** by providing leadership with a clean, queryable knowledge base for accurate analysis and reporting.

### **Practical, Real-World Use Cases**

This methodology is not theoretical. It is a direct, practical blueprint for solving a number of common, high-stakes challenges in the Third Sector, including:

*   **Legacy CRM Migration:** Safely migrating and cleaning years of supporter data from an old, unstructured spreadsheet system into a new, modern CRM like Salesforce or Raiser's Edge.
*   **Public Data Analysis:** Ingesting and processing unstructured public reports (e.g., from the Charity Commission or academic studies) to extract key trends and strategic insights.
*   **Beneficiary Feedback Processing:** Transforming thousands of lines of unstructured, qualitative feedback from surveys or interviews into a structured, thematically-tagged database for impact analysis.

---

### **The Technical Approach: A High-Level Look at the Method**

For those interested in the process, the method is an offline script that works like a highly organised and careful librarian, following three simple steps:

1.  **Step 1: It separates the useful information from the clutter.** The script first performs a high-speed pass to read the original messy files. It is programmed to identify and pull out the specific, timeless data it needs (like names, dates, and postcodes) while safely ignoring any surrounding information that is outdated, inconsistently formatted, or broken.

2.  **Step 2: It corrects and standardises the information.** The extracted data is then processed through a simple, rule-based cleaning process. This step uses a formal "house style" guide to correct common errors, such as making all dates follow the same format or fixing recurring misspellings, ensuring all the information is consistent.

3.  **Step 3: It carefully writes the final, clean record.** The pipeline's final stage uses a supervised software tool to act as a "master clerk." It takes the clean, validated data from the previous steps and is given a single, clear task: write a new, perfectly structured record into the central database. This final pass ensures the output is not just clean, but also consistent and easy for the team to use.

---

### **Technical Appendix: The Demonstration Script**
    
  For those interested in the practical implementation, a clean, well-commented Python script demonstrating the core methodology of this case study can be found in the `src` directory of this repository. The script is designed to be a self-contained, illustrative example, not a production-ready engine.
    
   [**View the script: `demo_data_cleaning_pipeline.py`**](./src/demo_data_cleaning_pipeline.py)

---

*Go back to the [**Main Portfolio Page**](https://github.com/seancasey-portfolio) or explore another case study:*
*   *[Turning Messy Spreadsheets into a Usable Database](https://github.com/seancasey-portfolio/Case-Study-Cleaning-Legacy-Data)*
*   *[Automating Internal Reports & Documentation](https://github.com/seancasey-portfolio/Case-Study-Automating-Internal-Documentation)*
*   *[Building Reliable & Well-Behaved AI Tools](https://github.com/seancasey-portfolio/Case-Study-Building-Reliable-AI-Tools)*
*   *[Transforming Raw Data into Compelling Stories](https://github.com/seancasey-portfolio/Case-Study-Data-To-Impact-Stories)*
