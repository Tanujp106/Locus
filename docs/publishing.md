# Publishing

Locus is portable-first. A skill can be copied or installed independently by a compatible Agent Skills client.

When a plugin is ready for native distribution:

1. Add its platform-specific plugin manifest.
2. Add the corresponding root marketplace entry.
3. Validate every manifest and local source path.
4. Test installation of the individual plugin.
5. Document permissions, external services, and required authentication.

Do not make marketplace metadata the canonical copy of skill instructions. The canonical content remains under `plugins/<name>/skills/`.
