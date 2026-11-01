import tkinter as tk
from tkinter import messagebox
from google_places import search_places
from excel_export import export_excel
from lead_score import calculate_score


def start_gui() -> None:
    root = tk.Tk()
    root.title("Cafe Lead Finder v1.0")
    root.geometry("500x420")
    root.resizable(False, False)

    # ── City field ──────────────────────────────────────────
    tk.Label(root, text="City", anchor="w").pack(fill="x", padx=20, pady=(20, 0))
    city_entry = tk.Entry(root, font=("Arial", 11))
    city_entry.pack(fill="x", padx=20)

    # ── Keyword field ────────────────────────────────────────
    tk.Label(root, text="Keyword", anchor="w").pack(fill="x", padx=20, pady=(10, 0))
    keyword_entry = tk.Entry(root, font=("Arial", 11))
    keyword_entry.insert(0, "Cafe")
    keyword_entry.pack(fill="x", padx=20)

    # ── Status label ─────────────────────────────────────────
    status_var = tk.StringVar(value="Ready.")
    tk.Label(root, textvariable=status_var, fg="gray", font=("Arial", 9)).pack(pady=(8, 0))

    results: list[dict] = []

    # ── Search ───────────────────────────────────────────────
    def search() -> None:
        nonlocal results
        keyword = keyword_entry.get().strip()
        city    = city_entry.get().strip()

        if not city:
            messagebox.showwarning("Missing Input", "Please enter a city name.")
            return
        if not keyword:
            messagebox.showwarning("Missing Input", "Please enter a keyword.")
            return

        status_var.set("Searching… please wait.")
        root.update_idletasks()

        results = search_places(keyword, city)

        if not results:
            status_var.set("No results found. Check your API key or try a different city.")
            messagebox.showinfo("No Results",
                                "No places found.\n"
                                "Make sure your API key is valid and the Places API is enabled.")
            return

        for item in results:
            item["score"] = calculate_score(item)
            item.setdefault("email", "")   # ensure key exists for DB save

        status_var.set(f"✓ Found {len(results)} places.")
        messagebox.showinfo("Search Complete", f"Found {len(results)} places.")

    # ── Export ───────────────────────────────────────────────
    def export() -> None:
        if not results:
            messagebox.showwarning("No Data",
                                   "No results to export.\n"
                                   "Run a search first.")
            return

        path = export_excel(results)
        status_var.set(f"✓ Saved to {path}")
        messagebox.showinfo("Export Complete", f"File saved to:\n{path}")

    # ── Buttons ──────────────────────────────────────────────
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=20)

    tk.Button(btn_frame, text="🔍  START SEARCH", command=search,
              width=20, height=2, bg="#4CAF50", fg="white",
              font=("Arial", 10, "bold")).pack(side="left", padx=10)

    tk.Button(btn_frame, text="📥  EXPORT EXCEL", command=export,
              width=20, height=2, bg="#2196F3", fg="white",
              font=("Arial", 10, "bold")).pack(side="left", padx=10)

    root.mainloop()
