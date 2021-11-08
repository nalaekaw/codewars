def number(lines):
    if lines:
        for i in range(len(lines)):
            lines[i] = f"{i+1}: {lines[i]}"
    return lines

# def number(lines):
#   return ['%d: %s' % v for v in enumerate(lines, 1)]

print(number(["a", "b", "c"]))
