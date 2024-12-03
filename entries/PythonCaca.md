# PythonCaca

PythonCaca is a programming *caca* that can be used both for **writing** **command-line scripts** or building **web applications**.

> As the legend says, caca

* Popo
* Defecacion
* EA

1. Zowie
2. Zuwie
3. Gerbil

``Use `code` in your Markdown file.``

```python
if search_raw.is_valid():
		if get_entry(search := str(search_raw.cleaned_data["search"]).lower().capitalize()):
				return redirect(reverse("encyclopedia:entry", args=(quote_plus(search))))
		else:
				if not (coincidences := [entry for entry in list_entries() if search.lower() in entry.lower()]):
						render_data["default"] = f"No coincidence found for '{search_raw.cleaned_data["search"]}' "
				else:
						render_data["coincidences"] = coincidences
		render_data["search"] = search
		render_data["search_raw"] = search_raw.cleaned_data["search"]
else:
		return redirect(reverse("encyclopedia:index"))
```

## Tremendo

### Fua

#### Pis

![Tremenda fotarda](https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/006.png)

[Nose](http://127.0.0.1:8000/wiki/edit/PythonCaca)