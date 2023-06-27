// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TemplateSheetDefinition
    {
        public readonly Pulumi.AwsNative.QuickSight.TemplateSheetContentType? ContentType;
        public readonly string? Description;
        public readonly ImmutableArray<Outputs.TemplateFilterControl> FilterControls;
        public readonly ImmutableArray<Outputs.TemplateLayout> Layouts;
        public readonly string? Name;
        public readonly ImmutableArray<Outputs.TemplateParameterControl> ParameterControls;
        public readonly ImmutableArray<Outputs.TemplateSheetControlLayout> SheetControlLayouts;
        public readonly string SheetId;
        public readonly ImmutableArray<Outputs.TemplateSheetTextBox> TextBoxes;
        public readonly string? Title;
        public readonly ImmutableArray<Outputs.TemplateVisual> Visuals;

        [OutputConstructor]
        private TemplateSheetDefinition(
            Pulumi.AwsNative.QuickSight.TemplateSheetContentType? contentType,

            string? description,

            ImmutableArray<Outputs.TemplateFilterControl> filterControls,

            ImmutableArray<Outputs.TemplateLayout> layouts,

            string? name,

            ImmutableArray<Outputs.TemplateParameterControl> parameterControls,

            ImmutableArray<Outputs.TemplateSheetControlLayout> sheetControlLayouts,

            string sheetId,

            ImmutableArray<Outputs.TemplateSheetTextBox> textBoxes,

            string? title,

            ImmutableArray<Outputs.TemplateVisual> visuals)
        {
            ContentType = contentType;
            Description = description;
            FilterControls = filterControls;
            Layouts = layouts;
            Name = name;
            ParameterControls = parameterControls;
            SheetControlLayouts = sheetControlLayouts;
            SheetId = sheetId;
            TextBoxes = textBoxes;
            Title = title;
            Visuals = visuals;
        }
    }
}
