---
icon: material/package-up
status: new
---

# DiSky v4.24 -> v4.25

DiSky v4.25.0 adds new labels and dropdown in modals, leading to breaking change on the way you would add text input to your modal.

Now, every component should be "wrapped" in a **label** component, and that's also this component that will define its actually displayed label:

## Before 4.25:

```applescript
# We would define the label when creating the input
set {_input} to new short text input with id "description" named "Description"

# then add the input directly to the modal
add {_input} to rows of modal
```

## Since 4.25:

```applescript
# Don't specify the label anymore when creating the input
set {_input} to new short text input with id "description"

# we have to make another component to wrap the input
set {_inputLabel} to new label "Description" with {_input}

# then add the inputLabel to the modal, NOT the input itself
add {_inputLabel} to rows of modal
```