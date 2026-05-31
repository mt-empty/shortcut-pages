# Shortcut-Pages Copilot Instructions

A collection of keyboard shortcuts for desktop applications, CLI tools, and websites, consumed by [shortcut clients](https://github.com/mt-empty/shortcut-rust-client).

## Project Structure

- `json/` - **Source of truth**: All shortcut pages as JSON files
- `GUI/` - Generated markdown files for GUI applications (built from `json/` + `GUI.txt`)
- `GUI.txt` - Whitelist of JSON files to include in GUI output
- `contribution/template.json` - JSON schema template for new pages

## JSON Page Format

Every shortcut page follows this structure (see `json/virtual-box.json` as reference):

```json
{
  "name": "Program Name",
  "description": "Program description",
  "metadata": { "sourceUrl": "https://..." },
  "aliases": ["alias-one", "alias-two"],
  "isGUI": true,
  "section_order": ["Section One", "Section Two"],
  "sections": {
    "Section One": [
      { "val": "Description", "key": "[Ctrl] [A]" }
    ]
  }
}
```

**Required fields**: `name`, `isGUI`, `metadata.sourceUrl`, `sections`
**Key format**: Use `[Modifier] [Key]` notation (e.g., `[Ctrl] [Shift] [S]`)

## Alias Rules

Aliases are alternative names to find the same page. **Restrictions**:
- No spaces (use hyphens: `visual-studio` not `visual studio`)
- Forbidden characters: ``+ < > \ / : * # $ % & { } ! ' ` " @ = |``
- Cannot duplicate the JSON filename

## Developer Workflow

### Validate a new/modified page
```bash
python3 validate_page.py json/your-page.json
```

### Convert JSON to markdown (for testing output)
```bash
python3 convert_to_page.py GUI/ json/your-page.json
```

### Build all GUI pages
```bash
./runParseJSON.sh
```

### Add a new GUI program
1. Create `json/program-name.json` following the template
2. Run `python3 validate_page.py json/program-name.json`
3. Add `program-name.json` to `GUI.txt` if it's a GUI application

## Markdown Output Format

The converter produces markdown with custom tags for client parsing:
- `# ` - Title
- `$ ` - Section/category header
- `` ` `` - Shortcut key prefix
- `{{description}}` - Description wrapper
- `> ` - Normal text (source URL, aliases)

## Alias Symlinks

When `convert_to_page.py` runs, it automatically creates symlinks in the output directory for each alias. For example, `virtual-box.json` with aliases `["virtualbox", "vbox"]` produces:
- `virtual-box.md` (main file)
- `virtualbox.md` → symlink to `virtual-box.md`
- `vbox.md` → symlink to `virtual-box.md`

This allows clients to find shortcuts by any alias name.

## CI/CD

Releases are triggered by version tags (`v*.*.*`). The workflow zips `GUI/*.md` files.
