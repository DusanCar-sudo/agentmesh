#!/bin/bash
# Cleanup script — run manually in terminal
# Frees ~4GB on system drive

echo "=== Starting cleanup ==="

# 1. Remove original models copy (already copied to DATA1)
rm -rf /home/dusan/models/dspark_qwen3_4b_block7
echo "1. Removed original models copy (~5.2GB freed)"

# 2. Delete old Claude Code copies (keep only ~/.local/lib)
sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code/
echo "2. Removed system Claude Code copy"

rm -rf ~/.config/Claude/claude-code/2.1.202/
echo "3. Removed old Claude Code 2.1.202"

# 3. Delete Thunderbird leftovers (app already uninstalled)
sudo rm -rf /var/snap/thunderbird/
echo "4. Removed /var/snap/thunderbird/"

rm -rf /home/dusan/thunderbird/
echo "5. Removed ~/thunderbird/"

rm -rf /home/dusan/snap/thunderbird/
echo "6. Removed ~/snap/thunderbird/"

# 4. Clean APT cache
sudo apt clean
echo "7. Cleaned APT cache"

echo ""
echo "=== Cleanup complete ==="
df -h /
