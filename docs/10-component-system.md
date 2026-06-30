# Component System

## Version 1.0

---

## Philosophy

A component is a reusable, self-contained unit of interface that performs a specific function.

Components are not just code. They are patterns. When a component is built well, it can be reused across multiple projects — reducing development time, increasing consistency, and allowing us to focus on the unique aspects of each client.

---

## Component Hierarchy

```
Pages
├── Layouts
│   ├── Navigation
│   ├── Hero
│   ├── Sections
│   │   ├── Cards
│   │   ├── Galleries
│   │   ├── Forms
│   │   └── Footers
│   └── Modals
├── Atoms
│   ├── Buttons
│   ├── Inputs
│   ├── Icons
│   ├── Typography
│   └── Dividers
└── Utilities
    ├── Animations
    ├── Spacing
    └── Grid
```

---

## Component Specification Format

Every component in the system must be documented with:

```
## Component Name

### Purpose
What does this component do? Why does it exist?

### When to Use
- Use case 1
- Use case 2

### When Not to Use
- Anti-case 1
- Anti-case 2

### Anatomy
- Element 1: description
- Element 2: description

### States
- Default
- Hover
- Focus
- Active
- Loading (if applicable)
- Error (if applicable)
- Disabled (if applicable)

### Variants
- Primary
- Secondary
- Ghost (if applicable)

### Accessibility
- ARIA roles
- Keyboard interactions
- Screen reader notes

### Example Code
```html
<!-- component markup -->
```

### Motion
- Entry animation
- Hover animation
- Exit animation

### Checklist
- [ ] Condition 1
- [ ] Condition 2
```

---

## Core Components

### Button

**Purpose:** Triggers an action. The most important interactive element.

**When to Use:**
- Primary CTA on the page (once)
- Secondary actions
- Form submissions

**When Not to Use:**
- For navigation links (use anchor tags styled as links)
- More than once as primary action per viewport

**Anatomy:**
```
Container:  <button> or <a>
Label:      text
Icon:       optional (left or right)
Spinner:    during loading state
```

**States:**
| State | CSS |
|---|---|
| Default | bg-accent, text-white, border-none, radius-md, px-6 py-3 |
| Hover | bg-accent-light, y: -1px, shadow-md, cursor-pointer |
| Focus | ring-2 ring-accent ring-offset-2 |
| Active | scale: 0.97 |
| Loading | spinner replaces label, disabled |
| Disabled | opacity 50%, cursor-not-allowed |

**Variants:**
```
Primary:    bg-accent, text-white
Secondary:  bg-transparent, border-accent, text-accent
Ghost:      bg-transparent, text-accent, no border
```

**Accessibility:**
- role="button" if using non-button element
- aria-label if icon-only
- aria-disabled when disabled
- Keyboard: Enter/Space to activate

---

### Card

**Purpose:** Groups related content into a digestible container.

**When to Use:**
- Services listing
- Features overview
- Portfolio grid
- Team members
- Pricing tiers

**Anatomy:**
```
Container:  <div> with border, radius, shadow
Image:      optional top image
Content:    heading + description + optional link
```

**States:**
| State | CSS |
|---|---|
| Default | border-subtle, shadow-sm |
| Hover | y: -8px, shadow-md, cursor-pointer |
| Focus | ring-2 ring-accent |

---

### Input

**Purpose:** Collects user text input.

**Anatomy:**
```
Label:      <label> with for attribute
Field:      <input> or <textarea>
Message:    optional helper/error/success text
Icon:       optional left icon
```

**States:**
| State | CSS |
|---|---|
| Default | border-medium, bg-transparent |
| Focus | border-accent, ring-1 ring-accent |
| Hover | border-dark |
| Filled | border-valid or border-invalid |
| Error | border-red, error message |
| Disabled | opacity 50% |

---

### Navigation

**Purpose:** Provides page/section navigation.

**Variants:**
| Variant | Use |
|---|---|
| Fixed top | Default, transparent → solid on scroll |
| Side | Dashboard, documentation |
| Bottom nav | Mobile-focused apps |

**States:**
| State | CSS |
|---|---|
| Default | transparent (in hero), white text |
| Scrolled | bg-blur, dark/light based on section |
| Active | accent underline or highlight |

---

### Footer

**Purpose:** Contains secondary navigation, contact info, legal links.

**Anatomy:**
```
Columns:    links (optional), contact, social
Bottom:     copyright + legal
```

---

## Component Checklist

- [ ] Component follows the specification format
- [ ] All interactive states defined (rest, hover, focus, active, disabled)
- [ ] Accessibility requirements documented
- [ ] Motion spec included
- [ ] Responsive behavior defined
- [ ] Variants documented
- [ ] Code example provided
- [ ] Anti-patterns listed

---

## Future Ideas

- Live component preview page with interactive state toggling
- Component usage analytics across projects
- "Component gap" analysis — identifying missing components across client projects
