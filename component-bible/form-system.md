# Component Bible: Form System

## Version 1.0

## Variants

| Variant | Use |
|---|---|
| Contact Form | Standard name + email + phone + message |
| Newsletter | Email only, minimal |
| Quote Request | Contact + project details + budget |
| Booking | Name + date + time + service selection |

## Field Types
```html
<!-- Text Input -->
<div class="form-group">
  <label for="field" class="block text-sm font-medium text-white mb-2">Label</label>
  <input type="text" id="field" name="field" required
         class="w-full px-4 py-3 bg-transparent border border-white/10 rounded-xl text-white
                focus:border-accent focus:ring-1 focus:ring-accent outline-none
                placeholder:text-gray-500 transition-all duration-200" />
  <p class="form-error text-sm text-red-400 mt-1 hidden" role="alert">Error message.</p>
</div>

<!-- Textarea -->
<textarea rows="4" class="w-full px-4 py-3 bg-transparent border border-white/10 rounded-xl
                focus:border-accent focus:ring-1 focus:ring-accent outline-none resize-none"></textarea>

<!-- Select -->
<select class="w-full px-4 py-3 bg-transparent border border-white/10 rounded-xl
               focus:border-accent focus:ring-1 focus:ring-accent outline-none">
  <option value="">Select an option</option>
</select>

<!-- Checkbox -->
<label class="flex items-start gap-3 cursor-pointer">
  <input type="checkbox" class="mt-1 accent-accent" />
  <span class="text-sm text-muted">I agree to the terms.</span>
</label>
```

## States
| State | Border | Text | Icon |
|---|---|---|---|
| Rest | white/10 | placeholder | none |
| Focus | accent + ring | — | — |
| Filled (valid) | green-500/50 | — | checkmark |
| Error | red-400 | red message | alert icon |
| Disabled | white/5 | opacity 50% | — |
