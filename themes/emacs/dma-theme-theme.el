;;; dma-theme-theme.el --- DMA Theme for Emacs -*- lexical-binding: t; -*-

;; Copyright (C) 2024 Dunsworth-Mann Analytics LLC
;; Author: Dunsworth-Mann Analytics LLC
;; URL: https://github.com/dunsworth-mann-analytics/dma-theme
;; Package-Requires: ((emacs "27.1"))
;; Version: 1.0.0
;; Keywords: faces, themes
;; This file is NOT part of GNU Emacs.

;;; Commentary:
;;
;; DMA Theme is a semantic color theme for Emacs focused on blues, teals,
;; turquoises, and greens with warm error/warning colors. It provides both
;; light and dark variants.
;;
;; To use:
;;   (add-to-list 'custom-theme-load-path "~/.emacs.d/themes/dma-theme")
;;   (load-theme 'dma-theme-light t)  ;; or 'dma-theme-dark
;;
;; For Doom Emacs:
;;   (package! dma-theme :recipe (:host github :repo "dunsworth-mann-analytics/dma-theme"))
;;   (setq doom-theme 'dma-theme-light)
;;
;; For Spacemacs:
;;   dotspacemacs-themes '(dma-theme-light)

;;; Code:

(deftheme dma-theme-light
  "DMA Theme Light - A semantic color theme focused on blues, teals, turquoises, and greens with warm error/warning colors."
  :author "Dunsworth-Mann Analytics LLC"
  :maintainer "Dunsworth-Mann Analytics LLC"
  :version "1.0.0"
  :url "https://github.com/dunsworth-mann-analytics/dma-theme"
  :package-version '(dma-theme . "1.0.0"))

;; Color palette for light theme
(let* (
  ;; Primary colors
  (dma-blue-900 "#002B5C")
  (dma-blue-800 "#003D7A")
  (dma-blue-700 "#00529E")
  (dma-blue-600 "#0069C0")
  (dma-blue-500 "#007BDB")
  (dma-blue-400 "#1A91E6")
  (dma-blue-300 "#4DA8EE")
  (dma-blue-200 "#8FC3F5")
  (dma-blue-100 "#C5DEF9")
  (dma-blue-50 "#E8F4FC")

  (dma-teal-900 "#004D4D")
  (dma-teal-800 "#006666")
  (dma-teal-700 "#007F7F")
  (dma-teal-600 "#009999")
  (dma-teal-500 "#00B3B3")
  (dma-teal-400 "#1ACCCC")
  (dma-teal-300 "#4DE5E5")
  (dma-teal-200 "#99F0F0")
  (dma-teal-100 "#CCF7F7")
  (dma-teal-50 "#E6FBFB")

  (dma-turquoise-900 "#005C5C")
  (dma-turquoise-800 "#007373")
  (dma-turquoise-700 "#008A8A")
  (dma-turquoise-600 "#00A1A1")
  (dma-turquoise-500 "#00B8B8")
  (dma-turquoise-400 "#1ACECE")
  (dma-turquoise-300 "#4DDDDD")
  (dma-turquoise-200 "#99EDED")
  (dma-turquoise-100 "#CCF6F6")
  (dma-turquoise-50 "#E6FBFB")

  (dma-green-900 "#004D1A")
  (dma-green-800 "#006622")
  (dma-green-700 "#007F2A")
  (dma-green-600 "#009933")
  (dma-green-500 "#00B33B")
  (dma-green-400 "#1ACC4D")
  (dma-green-300 "#4DD966")
  (dma-green-200 "#99E599")
  (dma-green-100 "#CCF0CC")
  (dma-green-50 "#E6F8E6")

  ;; Semantic colors
  (dma-error-900 "#7A0000")
  (dma-error-800 "#9E0000")
  (dma-error-700 "#C40000")
  (dma-error-600 "#E80000")
  (dma-error-500 "#FF1A1A")
  (dma-error-400 "#FF4D4D")
  (dma-error-300 "#FF7A7A")
  (dma-error-200 "#FFA8A8")
  (dma-error-100 "#FFD4D4")
  (dma-error-50 "#FFEAEA")

  (dma-warning-900 "#7A4A00")
  (dma-warning-800 "#9E5E00")
  (dma-warning-700 "#C47300")
  (dma-warning-600 "#E88800")
  (dma-warning-500 "#FF9F00")
  (dma-warning-400 "#FFAD33")
  (dma-warning-300 "#FFC466")
  (dma-warning-200 "#FFDB99")
  (dma-warning-100 "#FFF0CC")
  (dma-warning-50 "#FFF8E6")

  (dma-info-900 "#003D7A")
  (dma-info-800 "#00529E")
  (dma-info-700 "#0069C0")
  (dma-info-600 "#007BDB")
  (dma-info-500 "#0091E6")
  (dma-info-400 "#33A8EE")
  (dma-info-300 "#66BFFF")
  (dma-info-200 "#99D4FF")
  (dma-info-100 "#CCE9FF")
  (dma-info-50 "#E6F4FF")

  (dma-success-900 "#004D1A")
  (dma-success-800 "#006622")
  (dma-success-700 "#007F2A")
  (dma-success-600 "#009933")
  (dma-success-500 "#00B33B")
  (dma-success-400 "#33CC5A")
  (dma-success-300 "#66D97A")
  (dma-success-200 "#99E599")
  (dma-success-100 "#CCF0CC")
  (dma-success-50 "#E6F8E6")

  ;; Neutral colors
  (dma-bg "#F8FAFC")
  (dma-bg-alt "#F0F4F8")
  (dma-bg-elevated "#FFFFFF")
  (dma-fg "#1E282D")
  (dma-fg-muted "#485C6E")
  (dma-fg-subtle "#6E89A0")
  (dma-border "#C8D6E3")
  (dma-border-focus "#007BDB")
  (dma-selection "#C5DEF9")
  (dma-selection-fg "#002B5C")

  ;; UI colors
  (dma-cursor "#007BDB")
  (dma-line-number "#6E89A0")
  (dma-line-number-active "#00529E")
  (dma-highlight-line "#E8F4FC")
  (dma-region "#C5DEF9")

  ;; Syntax colors
  (dma-comment "#6E89A0")
  (dma-string "#007F2A")
  (dma-number "#00529E")
  (dma-keyword "#004D4D")
  (dma-keyword-control "#004D4D")
  (dma-storage "#004D4D")
  (dma-function "#00529E")
  (dma-variable "#1E282D")
  (dma-parameter "#485C6E")
  (dma-property "#1E282D")
  (dma-type "#006666")
  (dma-class "#006666")
  (dma-interface "#006666")
  (dma-namespace "#007F7F")
  (dma-constant "#7A4A00")
  (dma-operator "#004D4D")
  (dma-punctuation "#485C6E")
  (dma-bracket "#6E89A0")
  (dma-tag "#004D4D")
  (dma-attribute "#007F7F")
  (dma-regex "#7A4A00")
  (dma-escape "#E88800")
  (dma-annotation "#007F7F")
  (dma-decorator "#007F7F")

  ;; Git colors
  (dma-git-add "#009933")
  (dma-git-modified "#007BDB")
  (dma-git-deleted "#E80000")
  (dma-git-untracked "#009933")
  (dma-git-ignored "#6E89A0")
  (dma-git-conflict "#E88800")

  ;; Terminal ANSI colors
  (dma-term-black "#1E282D")
  (dma-term-red "#E80000")
  (dma-term-green "#009933")
  (dma-term-yellow "#E88800")
  (dma-term-blue "#007BDB")
  (dma-term-magenta "#007F7F")
  (dma-term-cyan "#00B3B3")
  (dma-term-white "#C8D6E3")
  (dma-term-bright-black "#485C6E")
  (dma-term-bright-red "#FF1A1A")
  (dma-term-bright-green "#00B33B")
  (dma-term-bright-yellow "#FF9F00")
  (dma-term-bright-blue "#1A91E6")
  (dma-term-bright-magenta "#1ACECE")
  (dma-term-bright-cyan "#4DDDDD")
  (dma-term-bright-white "#F0F4F8")
)

(custom-theme-set-faces
 'dma-theme-light

 ;; Core faces
 `(default ((t (:foreground ,dma-fg :background ,dma-bg))))
 `(cursor ((t (:background ,dma-cursor :foreground ,dma-bg))))
 `(cursor-in-non-selected-windows ((t (:background ,dma-fg-subtle :foreground ,dma-bg))))

 ;; Background/Region
 `(region ((t (:background ,dma-region :foreground ,dma-selection-fg))))
 `(highlight ((t (:background ,dma-selection :foreground ,dma-selection-fg))))
 `(lazy-highlight ((t (:background ,dma-highlight-line :foreground ,dma-fg))))
 `(secondary-selection ((t (:background ,dma-bg-alt :foreground ,dma-fg))))

 ;; Line numbers
 `(linum ((t (:foreground ,dma-line-number :background ,dma-bg))))
 `(line-number ((t (:foreground ,dma-line-number :background ,dma-bg))))
 `(line-number-current-line ((t (:foreground ,dma-line-number-active :background ,dma-bg :weight bold))))

 ;; Highlight current line
 `(hl-line ((t (:background ,dma-highlight-line))))
 `(hl-line-face ((t (:background ,dma-highlight-line))))

 ;; Fringe
 `(fringe ((t (:background ,dma-bg))))
 `(fringe-cursor ((t (:background ,dma-cursor))))
 `(fringe-bitmap ((t (:foreground ,dma-fg-subtle :background ,dma-bg))))

 ;; Mode line
 `(mode-line ((t (:foreground ,dma-fg :background ,dma-bg-alt :box nil))))
 `(mode-line-inactive ((t (:foreground ,dma-fg-subtle :background ,dma-bg :box nil))))
 `(mode-line-buffer-id ((t (:foreground ,dma-fg :background ,dma-bg-alt :weight bold))))
 `(mode-line-position ((t (:foreground ,dma-fg-subtle :background ,dma-bg-alt))))
 `(mode-line-misc-info ((t (:foreground ,dma-fg-subtle :background ,dma-bg-alt))))
 `(mode-line-remote ((t (:foreground ,dma-fg :background ,dma-bg-alt :weight bold :underline t))))

 ;; Header line
 `(header-line ((t (:foreground ,dma-fg :background ,dma-bg-alt :box nil))))
 `(header-line-highlight ((t (:foreground ,dma-fg :background ,dma-bg-alt :box nil))))

 ;; Minibuffer
 `(minibuffer-prompt ((t (:foreground ,dma-cursor :weight bold))))
 `(minibuffer-completion-table ((t (:foreground ,dma-fg-subtle))))
 `(minibuffer-completion-confirm ((t (:foreground ,dma-success-500 :weight bold))))

 ;; Completion
 `(completions-first-difference ((t (:foreground ,dma-cursor :weight bold))))
 `(completions-common-part ((t (:foreground ,dma-fg))))
 `(completions-annotations ((t (:foreground ,dma-fg-subtle))))

 ;; Menu
 `(menu ((t (:foreground ,dma-fg :background ,dma-bg-elevated))))
 `(menu-bar ((t (:foreground ,dma-fg :background ,dma-bg-alt :box (:line-width 1 :color ,dma-border :style released-buttons)))))
 `(menu-separator ((t (:background ,dma-border))))
 `(menu-highlight ((t (:foreground ,dma-fg :background ,dma-selection :box nil))))

 ;; Tool bar
 `(tool-bar ((t (:background ,dma-bg-alt))))
 `(tool-bar-border ((t (:foreground ,dma-border))))
 `(tool-bar-button ((t (:background ,dma-bg-alt :box (:line-width 1 :color ,dma-border :style released-buttons)))))
 `(tool-bar-button-selected ((t (:background ,dma-selection :box (:line-width 1 :color ,dma-border-focus :style pressed-buttons)))))

 ;; Tooltip
 `(tooltip ((t (:foreground ,dma-fg :background ,dma-bg-elevated :box (:line-width 1 :color ,dma-border)))))

 ;; Scroll bar
 `(scroll-bar ((t (:background ,dma-bg-alt :foreground ,dma-fg-subtle))))
 `(vertical-scroll-bar ((t (:background ,dma-bg-alt :foreground ,dma-fg-subtle))))
 `(horizontal-scroll-bar ((t (:background ,dma-bg-alt :foreground ,dma-fg-subtle))))

 ;; Window dividers
 `(window-divider ((t (:foreground ,dma-border))))
 `(window-divider-first-pixel ((t (:foreground ,dma-border))))
 `(window-divider-last-pixel ((t (:foreground ,dma-border))))

 ;; Tab bar
 `(tab-bar ((t (:background ,dma-bg-alt))))
 `(tab-bar-button ((t (:foreground ,dma-fg-subtle :background ,dma-bg-alt))))
 `(tab-bar-button-highlight ((t (:foreground ,dma-cursor :background ,dma-selection))))
 `(tab-bar-tab ((t (:foreground ,dma-fg-subtle :background ,dma-bg-alt :box (:line-width 1 :color ,dma-border :style released-buttons)))))
 `(tab-bar-tab-selected ((t (:foreground ,dma-fg :background ,dma-bg :box (:line-width 2 :color ,dma-cursor :style released-buttons) :weight bold))))
 `(tab-bar-tab-inactive ((t (:foreground ,dma-fg-subtle :background ,dma-bg-alt :box (:line-width 1 :color ,dma-border :style released-buttons)))))

 ;; Buttons
 `(button ((t (:foreground ,dma-bg :background ,dma-cursor :weight bold :underline t))))
 `(button-alt ((t (:foreground ,dma-cursor :background ,dma-bg :weight bold :underline t))))

 ;; Links
 `(link ((t (:foreground ,dma-cursor :underline t))))
 `(link-visited ((t (:foreground ,dma-teal-700 :underline t))))

 ;; Matching parens
 `(show-paren-match ((t (:background ,dma-selection :foreground ,dma-selection-fg :weight bold))))
 `(show-paren-mismatch ((t (:background ,dma-error-100 :foreground ,dma-error-500 :weight bold))))

 ;; Search
 `(isearch ((t (:background ,dma-warning-100 :foreground ,dma-warning-900))))
 `(isearch-fail ((t (:background ,dma-error-100 :foreground ,dma-error-500))))
 `(lazy-highlight ((t (:background ,dma-highlight-line :foreground ,dma-fg))))

 ;; Query replace
 `(query-replace ((t (:background ,dma-warning-100 :foreground ,dma-warning-900 :weight bold))))
 `(query-replace-replacement ((t (:background ,dma-info-100 :foreground ,dma-info-900))))

 ;; Compilation/Grep
 `(compilation-error ((t (:foreground ,dma-error-500 :weight bold))))
 `(compilation-warning ((t (:foreground ,dma-warning-500 :weight bold))))
 `(compilation-info ((t (:foreground ,dma-info-500 :weight bold))))
 `(compilation-line-number ((t (:foreground ,dma-fg-subtle))))
 `(compilation-column-number ((t (:foreground ,dma-fg-subtle))))
 `(compilation-file-name ((t (:foreground ,dma-function :underline t))))

 ;; Diff
 `(diff-header ((t (:foreground ,dma-comment))))
 `(diff-file-header ((t (:foreground ,dma-function :weight bold))))
 `(diff-index ((t (:foreground ,dma-keyword))))
 `(diff-hunk-header ((t (:foreground ,dma-keyword-control :weight bold))))
 `(diff-added ((t (:foreground ,dma-git-add :background ,dma-success-50))))
 `(diff-removed ((t (:foreground ,dma-git-deleted :background ,dma-error-50))))
 `(diff-changed ((t (:foreground ,dma-git-modified :background ,dma-info-50))))
 `(diff-context ((t (:foreground ,dma-fg-subtle :background ,dma-bg))))

 ;; Version control
 `(vc-dir-up-to-date-header ((t (:foreground ,dma-git-add))))
 `(vc-dir-modified-header ((t (:foreground ,dma-git-modified))))
 `(vc-dir-conflict-header ((t (:foreground ,dma-git-conflict))))
 `(vc-dir-ignore-header ((t (:foreground ,dma-git-ignored))))

 ;; Font lock (syntax highlighting)
 `(font-lock-comment-face ((t (:foreground ,dma-comment :slant italic))))
 `(font-lock-comment-delimiter-face ((t (:foreground ,dma-comment :slant italic))))
 `(font-lock-doc-face ((t (:foreground ,dma-comment :slant italic))))
 `(font-lock-doc-string-face ((t (:foreground ,dma-string))))
 `(font-lock-string-face ((t (:foreground ,dma-string))))
 `(font-lock-string-delimiter-face ((t (:foreground ,dma-string))))
 `(font-lock-constant-face ((t (:foreground ,dma-constant))))
 `(font-lock-variable-name-face ((t (:foreground ,dma-variable))))
 `(font-lock-function-name-face ((t (:foreground ,dma-function :weight bold))))
 `(font-lock-keyword-face ((t (:foreground ,dma-keyword :weight bold))))
 `(font-lock-control-flow-face ((t (:foreground ,dma-keyword-control :weight bold))))
 `(font-lock-type-face ((t (:foreground ,dma-type :weight bold))))
 `(font-lock-builtin-face ((t (:foreground ,dma-function))))
 `(font-lock-preprocessor-face ((t (:foreground ,dma-annotation))))
 `(font-lock-negation-char-face ((t (:foreground ,dma-operator :weight bold))))
 `(font-lock-regexp-grouping-backslash ((t (:foreground ,dma-escape :weight bold))))
 `(font-lock-regexp-grouping-construct ((t (:foreground ,dma-regex))))
 `(font-lock-escape-face ((t (:foreground ,dma-escape :weight bold))))
 `(font-lock-warning-face ((t (:foreground ,dma-error-500 :weight bold))))
 `(font-lock-declaration-face ((t (:foreground ,dma-type :weight bold))))
 `(font-lock-doc-markup-face ((t (:foreground ,dma-keyword))))
 `(font-lock-comment-face ((t (:foreground ,dma-comment :slant italic))))

 ;; Tree-sitter faces (if available)
 `(treesitter-font-lock-comment-face ((t (:foreground ,dma-comment :slant italic))))
 `(treesitter-font-lock-string-face ((t (:foreground ,dma-string))))
 `(treesitter-font-lock-number-face ((t (:foreground ,dma-number))))
 `(treesitter-font-lock-keyword-face ((t (:foreground ,dma-keyword :weight bold))))
 `(treesitter-font-lock-function-face ((t (:foreground ,dma-function :weight bold))))
 `(treesitter-font-lock-type-face ((t (:foreground ,dma-type :weight bold))))
 `(treesitter-font-lock-variable-face ((t (:foreground ,dma-variable))))
 `(treesitter-font-lock-constant-face ((t (:foreground ,dma-constant))))
 `(treesitter-font-lock-operator-face ((t (:foreground ,dma-operator))))
 `(treesitter-font-lock-punctuation-face ((t (:foreground ,dma-punctuation))))
 `(treesitter-font-lock-property-face ((t (:foreground ,dma-property))))
 `(treesitter-font-lock-tag-face ((t (:foreground ,dma-tag))))

 ;; Org mode
 `(org-document-title ((t (:foreground ,dma-fg :weight bold :height 1.4))))
 `(org-document-info ((t (:foreground ,dma-fg-subtle))))
 `(org-document-info-keyword ((t (:foreground ,dma-keyword))))
 `(org-meta-line ((t (:foreground ,dma-comment))))
 `(org-tag ((t (:foreground ,dma-attribute :weight bold :background ,dma-bg-alt :box (:line-width 1 :color ,dma-border :style released-buttons)))))
 `(org-priority-a ((t (:foreground ,dma-error-500 :weight bold))))
 `(org-priority-b ((t (:foreground ,dma-warning-500 :weight bold))))
 `(org-priority-c ((t (:foreground ,dma-info-500 :weight bold))))
 `(org-headline-done ((t (:foreground ,dma-success-500 :weight bold :strike-through t))))
 `(org-todo ((t (:foreground ,dma-error-500 :weight bold))))
 `(org-scheduled ((t (:foreground ,dma-info-500))))
 `(org-deadline ((t (:foreground ,dma-warning-500))))
 `(org-timestamp ((t (:foreground ,dma-fg-subtle))))
 `(org-timestamp-active ((t (:foreground ,dma-cursor))))
 `(org-link ((t (:foreground ,dma-cursor :underline t))))
 `(org-url ((t (:foreground ,dma-cursor :underline t))))
 `(org-code ((t (:foreground ,dma-string :background ,dma-bg-alt))))
 `(org-verbatim ((t (:foreground ,dma-string :background ,dma-bg-alt))))
 `(org-block ((t (:foreground ,dma-fg-subtle))))
 `(org-block-begin-line ((t (:foreground ,dma-keyword :weight bold))))
 `(org-block-end-line ((t (:foreground ,dma-keyword :weight bold))))
 `(org-quote ((t (:foreground ,dma-comment :slant italic))))
 `(org-verse ((t (:foreground ,dma-comment :slant italic))))
 `(org-meta-line ((t (:foreground ,dma-comment))))

 ;; Markdown
 `(markdown-heading-face ((t (:foreground ,dma-markup-heading :weight bold))))
 `(markdown-heading-1-face ((t (:foreground ,dma-markup-heading :weight bold :height 2.0))))
 `(markdown-heading-2-face ((t (:foreground ,dma-markup-heading :weight bold :height 1.6))))
 `(markdown-heading-3-face ((t (:foreground ,dma-markup-heading :weight bold :height 1.4))))
 `(markdown-heading-4-face ((t (:foreground ,dma-markup-heading :weight bold :height 1.2))))
 `(markdown-heading-5-face ((t (:foreground ,dma-markup-heading :weight bold :height 1.1))))
 `(markdown-heading-6-face ((t (:foreground ,dma-markup-heading :weight bold :height 1.0))))
 `(markdown-code-face ((t (:foreground ,dma-string :background ,dma-bg-alt))))
 `(markdown-code-block-face ((t (:foreground ,dma-string :background ,dma-bg-alt))))
 `(markdown-link-face ((t (:foreground ,dma-cursor :underline t))))
 `(markdown-url-face ((t (:foreground ,dma-cursor :underline t))))

 ;; Magit
 `(magit-branch-current ((t (:foreground ,dma-git-add :weight bold))))
 `(magit-branch-local ((t (:foreground ,dma-fg))))
 `(magit-branch-remote ((t (:foreground ,dma-fg-subtle))))
 `(magit-branch-tag ((t (:foreground ,dma-attribute))))
 `(magit-diff-added ((t (:foreground ,dma-git-add :background ,dma-success-50))))
 `(magit-diff-removed ((t (:foreground ,dma-git-deleted :background ,dma-error-50))))
 `(magit-diff-context ((t (:foreground ,dma-fg-subtle))))
 `(magit-diff-heading ((t (:foreground ,dma-keyword-control :weight bold))))
 `(magit-diff-file-heading ((t (:foreground ,dma-function :weight bold))))
 `(magit-diff-hunk-heading ((t (:foreground ,dma-keyword :weight bold))))
 `(magit-section-heading ((t (:foreground ,dma-fg :weight bold))))
 `(magit-status-heading ((t (:foreground ,dma-fg :weight bold))))
 `(magit-status-unpushed-to-push ((t (:foreground ,dma-git-add))))
 `(magit-status-unpushed-to-upstream ((t (:foreground ,dma-git-add))))
 `(magit-status-unpulled-from-upstream ((t (:foreground ,dma-git-modified))))
 `(magit-status-recent-commit ((t (:foreground ,dma-fg))))

 ;; Flycheck/Flymake
 `(flycheck-error ((t (:foreground ,dma-error-500 :underline (:style wave :color ,dma-error-500)))))
 `(flycheck-warning ((t (:foreground ,dma-warning-500 :underline (:style wave :color ,dma-warning-500)))))
 `(flycheck-info ((t (:foreground ,dma-info-500 :underline (:style wave :color ,dma-info-500)))))

 ;; Company
 `(company-tooltip ((t (:foreground ,dma-fg :background ,dma-bg-elevated))))
 `(company-tooltip-selection ((t (:background ,dma-selection :foreground ,dma-selection-fg))))
 `(company-tooltip-common ((t (:foreground ,dma-cursor :weight bold))))
 `(company-tooltip-detail ((t (:foreground ,dma-fg-subtle :background ,dma-bg-elevated))))
 `(company-preview ((t (:foreground ,dma-fg :background ,dma-bg-elevated :box (:line-width 1 :color ,dma-border)))))
 `(company-preview-common ((t (:foreground ,dma-cursor :weight bold))))

 ;; Ido
 `(ido-first-match ((t (:foreground ,dma-cursor :weight bold :background ,dma-selection))))
 `(ido-only-match ((t (:foreground ,dma-cursor :weight bold :background ,dma-selection))))
 `(ido-subdir ((t (:foreground ,dma-fg-subtle))))
 `(ido-indicator ((t (:foreground ,dma-warning-500 :weight bold))))

 ;; Helm
 `(helm-header ((t (:foreground ,dma-fg :weight bold :background ,dma-bg-alt))))
 `(helm-source-header ((t (:foreground ,dma-keyword :weight bold :background ,dma-bg-alt))))
 `(helm-candidate-number ((t (:foreground ,dma-fg-subtle))))
 `(helm-selection ((t (:background ,dma-selection :foreground ,dma-selection-fg))))

 ;; Ivy
 `(ivy-current-match ((t (:background ,dma-selection :foreground ,dma-selection-fg :weight bold))))
 `(ivy-minibuffer-match-face-1 ((t (:foreground ,dma-cursor :weight bold))))
 `(ivy-minibuffer-match-face-2 ((t (:foreground ,dma-teal-500 :weight bold))))
 `(ivy-minibuffer-match-face-3 ((t (:foreground ,dma-turquoise-500 :weight bold))))
 `(ivy-minibuffer-match-face-4 ((t (:foreground ,dma-green-500 :weight bold))))
 `(ivy-minibuffer-match-face-5 ((t (:foreground ,dma-warning-500 :weight bold))))

 ;; Eglot/LSP
 `(eglot-error-highlight-face ((t (:underline (:style wave :color ,dma-error-500)))))
 `(eglot-warning-highlight-face ((t (:underline (:style wave :color ,dma-warning-500)))))
 `(eglot-info-highlight-face ((t (:underline (:style wave :color ,dma-info-500)))))
 `(eglot-hint-highlight-face ((t (:underline (:style wave :color ,dma-success-500)))))

 ;; LSP mode
 `(lsp-ui-doc-header ((t (:foreground ,dma-fg :weight bold :background ,dma-bg-alt))))
 `(lsp-ui-doc-markup-code-face ((t (:foreground ,dma-string :background ,dma-bg-alt))))
 `(lsp-ui-sideline-code-action ((t (:foreground ,dma-success-500))))
 `(lsp-ui-sideline-diagnostics ((t (:foreground ,dma-error-500))))

 ;; Projectile
 `(projectile-mode-line ((t (:foreground ,dma-fg :background ,dma-bg-alt))))
 `(projectile-project-name ((t (:foreground ,dma-function :weight bold))))

 ;; Dired
 `(dired-header ((t (:foreground ,dma-comment))))
 `(dired-directory ((t (:foreground ,dma-function :weight bold))))
 `(dired-symlink ((t (:foreground ,dma-turquoise-500))))
 `(dired-executable ((t (:foreground ,dma-success-500 :weight bold))))
 `(dired-warning ((t (:foreground ,dma-warning-500))))
 `(dired-ignored ((t (:foreground ,dma-fg-subtle))))

 ;; Eshell
 `(eshell-prompt ((t (:foreground ,dma-cursor :weight bold))))
 `(eshell-input-face ((t (:foreground ,dma-fg))))
 `(eshell-output-face ((t (:foreground ,dma-fg))))
 `(eshell-error-face ((t (:foreground ,dma-error-500))))

 ;; Shell
 `(shell-prompt-face ((t (:foreground ,dma-cursor :weight bold))))
 `(shell-output-face ((t (:foreground ,dma-fg))))
 `(shell-error-face ((t (:foreground ,dma-error-500))))

 ;; Term
 `(term-color-black ((t (:foreground ,dma-term-black))))
 `(term-color-red ((t (:foreground ,dma-term-red))))
 `(term-color-green ((t (:foreground ,dma-term-green))))
 `(term-color-yellow ((t (:foreground ,dma-term-yellow))))
 `(term-color-blue ((t (:foreground ,dma-term-blue))))
 `(term-color-magenta ((t (:foreground ,dma-term-magenta))))
 `(term-color-cyan ((t (:foreground ,dma-term-cyan))))
 `(term-color-white ((t (:foreground ,dma-term-white))))
 `(term-color-underline ((t (:underline t))))
 `(term-color-bold ((t (:weight bold))))
 `(term-color-reverse ((t (:inverse-video t))))

 ;; ANSI colors for term
 `(ansi-color-names-vector
   [,dma-term-black ,dma-term-red ,dma-term-green ,dma-term-yellow
    ,dma-term-blue ,dma-term-magenta ,dma-term-cyan ,dma-term-white
    ,dma-term-bright-black ,dma-term-bright-red ,dma-term-bright-green
    ,dma-term-bright-yellow ,dma-term-bright-blue ,dma-term-bright-magenta
    ,dma-term-bright-cyan ,dma-term-bright-white])

 ;; Outline
 `(outline-1 ((t (:foreground ,dma-markup-heading :weight bold :height 1.5))))
 `(outline-2 ((t (:foreground ,dma-markup-heading :weight bold :height 1.3))))
 `(outline-3 ((t (:foreground ,dma-markup-heading :weight bold :height 1.1))))
 `(outline-4 ((t (:foreground ,dma-markup-heading :weight bold :height 1.0))))

 ;; Which-key
 `(which-key-key-face ((t (:foreground ,dma-function :weight bold))))
 `(which-key-group-face ((t (:foreground ,dma-keyword))))
 `(which-key-desc-face ((t (:foreground ,dma-fg))))
 `(which-key-separator-face ((t (:foreground ,dma-comment))))

 ;; Consult
 `(consult-preview-key-face ((t (:foreground ,dma-cursor :weight bold))))
 `(consult-preview-line-face ((t (:foreground ,dma-fg))))

 ;; Corfu
 `(corfu-highlight-face ((t (:background ,dma-selection :foreground ,dma-selection-fg))))

 ;; Vertico
 `(vertico-current ((t (:background ,dma-selection :foreground ,dma-selection-fg :weight bold))))
 `(vertico-count ((t (:foreground ,dma-fg-subtle))))

 ;; Marginalia
 `(marginalia-annotation-face ((t (:foreground ,dma-fg-subtle))))
 `(marginalia-separator-face ((t (:foreground ,dma-comment))))

 ;; Embedded languages (web-mode, etc.)
 `(web-mode-html-tag-face ((t (:foreground ,dma-tag))))
 `(web-mode-html-attr-name-face ((t (:foreground ,dma-attribute))))
 `(web-mode-html-attr-value-face ((t (:foreground ,dma-string))))
 `(web-mode-css-selector-face ((t (:foreground ,dma-function))))
 `(web-mode-css-property-face ((t (:foreground ,dma-attribute))))
 `(web-mode-css-value-face ((t (:foreground ,dma-string))))
 `(web-mode-javascript-face ((t (:foreground ,dma-fg))))
 `(web-mode-javascript-variable-face ((t (:foreground ,dma-variable))))
 `(web-mode-javascript-function-face ((t (:foreground ,dma-function))))
 `(web-mode-javascript-keyword-face ((t (:foreground ,dma-keyword))))

 ;; Typescript
 `(typescript-face ((t (:foreground ,dma-fg))))
 `(typescript-keyword-face ((t (:foreground ,dma-keyword))))
 `(typescript-function-face ((t (:foreground ,dma-function))))
 `(typescript-type-face ((t (:foreground ,dma-type))))
 `(typescript-interface-face ((t (:foreground ,dma-interface))))
 `(typescript-variable-face ((t (:foreground ,dma-variable))))

 ;; Python
 `(python-face ((t (:foreground ,dma-fg))))
 `(python-keyword-face ((t (:foreground ,dma-keyword))))
 `(python-function-face ((t (:foreground ,dma-function))))
 `(python-class-face ((t (:foreground ,dma-class))))
 `(python-decorator-face ((t (:foreground ,dma-decorator))))
 `(python-string-face ((t (:foreground ,dma-string))))
 `(python-comment-face ((t (:foreground ,dma-comment :slant italic))))
 `(python-builtin-face ((t (:foreground ,dma-function))))
 `(python-self-face ((t (:foreground ,dma-variable :slant italic))))

 ;; Rust
 `(rust-face ((t (:foreground ,dma-fg))))
 `(rust-keyword-face ((t (:foreground ,dma-keyword))))
 `(rust-function-face ((t (:foreground ,dma-function))))
 `(rust-type-face ((t (:foreground ,dma-type))))
 `(rust-struct-face ((t (:foreground ,dma-type))))
 `(rust-enum-face ((t (:foreground ,dma-type))))
 `(rust-macro-face ((t (:foreground ,dma-decorator))))
 `(rust-attribute-face ((t (:foreground ,dma-annotation))))
 `(rust-lifetime-face ((t (:foreground ,dma-turquoise-500))))
 `(rust-string-face ((t (:foreground ,dma-string))))
 `(rust-comment-face ((t (:foreground ,dma-comment :slant italic))))
 `(rust-number-face ((t (:foreground ,dma-number))))

 ;; Go
 `(go-face ((t (:foreground ,dma-fg))))
 `(go-keyword-face ((t (:foreground ,dma-keyword))))
 `(go-function-face ((t (:foreground ,dma-function))))
 `(go-type-face ((t (:foreground ,dma-type))))
 `(go-struct-face ((t (:foreground ,dma-type))))
 `(go-interface-face ((t (:foreground ,dma-interface))))
 `(go-method-face ((t (:foreground ,dma-method))))
 `(go-field-face ((t (:foreground ,dma-property))))
 `(go-string-face ((t (:foreground ,dma-string))))
 `(go-comment-face ((t (:foreground ,dma-comment :slant italic))))
 `(go-number-face ((t (:foreground ,dma-number))))

 ;; C/C++
 `(c-face ((t (:foreground ,dma-fg))))
 `(c-keyword-face ((t (:foreground ,dma-keyword))))
 `(c-function-face ((t (:foreground ,dma-function))))
 `(c-type-face ((t (:foreground ,dma-type))))
 `(c-string-face ((t (:foreground ,dma-string))))
 `(c-comment-face ((t (:foreground ,dma-comment :slant italic))))
 `(c-preprocessor-face ((t (:foreground ,dma-annotation))))
 `(c-number-face ((t (:foreground ,dma-number))))

 ;; Java
 `(java-face ((t (:foreground ,dma-fg))))
 `(java-keyword-face ((t (:foreground ,dma-keyword))))
 `(java-function-face ((t (:foreground ,dma-function))))
 `(java-type-face ((t (:foreground ,dma-type))))
 `(java-annotation-face ((t (:foreground ,dma-annotation))))
 `(java-string-face ((t (:foreground ,dma-string))))
 `(java-comment-face ((t (:foreground ,dma-comment :slant italic))))

 ;; SQL
 `(sql-face ((t (:foreground ,dma-fg))))
 `(sql-keyword-face ((t (:foreground ,dma-keyword :weight bold))))
 `(sql-function-face ((t (:foreground ,dma-function))))
 `(sql-type-face ((t (:foreground ,dma-type))))
 `(sql-string-face ((t (:foreground ,dma-string))))
 `(sql-comment-face ((t (:foreground ,dma-comment :slant italic))))

 ;; YAML
 `(yaml-face ((t (:foreground ,dma-fg))))
 `(yaml-key-face ((t (:foreground ,dma-attribute))))
 `(yaml-value-face ((t (:foreground ,dma-string))))
 `(yaml-keyword-face ((t (:foreground ,dma-keyword))))

 ;; JSON
 `(json-face ((t (:foreground ,dma-fg))))
 `(json-keyword-face ((t (:foreground ,dma-keyword))))
 `(json-string-face ((t (:foreground ,dma-string))))
 `(json-number-face ((t (:foreground ,dma-number))))
 `(json-boolean-face ((t (:foreground ,dma-number))))

 ;; TOML
 `(toml-face ((t (:foreground ,dma-fg))))
 `(toml-key-face ((t (:foreground ,dma-attribute))))
 `(toml-value-face ((t (:foreground ,dma-string))))
 `(toml-keyword-face ((t (:foreground ,dma-keyword))))

 ;; Dockerfile
 `(dockerfile-face ((t (:foreground ,dma-fg))))
 `(dockerfile-keyword-face ((t (:foreground ,dma-keyword))))
 `(dockerfile-command-face ((t (:foreground ,dma-function))))

 ;; Makefile
 `(makefile-face ((t (:foreground ,dma-fg))))
 `(makefile-target-face ((t (:foreground ,dma-function :weight bold))))
 `(makefile-variable-face ((t (:foreground ,dma-variable))))
 `(makefile-command-face ((t (:foreground ,dma-string))))

 ;; Shell script
 `(sh-face ((t (:foreground ,dma-fg))))
 `(sh-keyword-face ((t (:foreground ,dma-keyword))))
 `(sh-function-face ((t (:foreground ,dma-function))))
 `(sh-variable-face ((t (:foreground ,dma-variable))))
 `(sh-string-face ((t (:foreground ,dma-string))))
 `(sh-comment-face ((t (:foreground ,dma-comment :slant italic))))

 ;; R
 `(ess-r-keyword-face ((t (:foreground ,dma-keyword))))
 `(ess-r-function-face ((t (:foreground ,dma-function))))
 `(ess-r-operator-face ((t (:foreground ,dma-operator))))
 `(ess-r-string-face ((t (:foreground ,dma-string))))
 `(ess-r-comment-face ((t (:foreground ,dma-comment :slant italic))))
 `(ess-r-number-face ((t (:foreground ,dma-number))))

 ;; Julia
 `(julia-face ((t (:foreground ,dma-fg))))
 `(julia-keyword-face ((t (:foreground ,dma-keyword))))
 `(julia-function-face ((t (:foreground ,dma-function))))
 `(julia-type-face ((t (:foreground ,dma-type))))
 `(julia-string-face ((t (:foreground ,dma-string))))
 `(julia-comment-face ((t (:foreground ,dma-comment :slant italic))))
 `(julia-number-face ((t (:foreground ,dma-number))))
)

(custom-theme-set-variables
 'dma-theme-light
 '(ansi-color-names-vector
   [,dma-term-black ,dma-term-red ,dma-term-green ,dma-term-yellow
    ,dma-term-blue ,dma-term-magenta ,dma-term-cyan ,dma-term-white
    ,dma-term-bright-black ,dma-term-bright-red ,dma-term-bright-green
    ,dma-term-bright-yellow ,dma-term-bright-blue ,dma-term-bright-magenta
    ,dma-term-bright-cyan ,dma-term-bright-white])
 '(cursor-type '(bar . 2))
 '(cursor-blink-timeout 10)
 '(blink-cursor-blinks 10)
 '(display-line-numbers t)
 '(display-line-numbers-width-start 4)
 '(display-line-numbers-width 5)
 '(display-fill-column-indicator-column 100)
 '(fill-column-indicator-column 100)
 '(show-trailing-whitespace t)
 '(indicate-empty-lines t)
 '(indicate-buffer-boundaries 'left)
 '(tab-width 2)
 '(indent-tabs-mode nil)
 '(xterm-mouse-mode t)
 '(mouse-wheel-scroll-amount '(1 ((shift) . 1) ((control) . nil)))
 '(mouse-wheel-progressive-speed nil)
 '(mouse-wheel-follow-mouse 't)
 '(scroll-conservatively 101)
 '(scroll-margin 3)
 '(scroll-step 1)
 '(auto-fill-function 'do-auto-fill)
 '(fill-column 100)
 '(sentence-end-double-space nil)
 '(require-final-newline t)
 '(add-log-time-format "%Y-%m-%d %H:%M ")
 '(add-log-full-name "Dunsworth-Mann Analytics LLC")
 '(add-log-mailing-address "https://dunsworth-mann.com"))

(provide-theme 'dma-theme-light)

;;; dma-theme-theme.el ends here