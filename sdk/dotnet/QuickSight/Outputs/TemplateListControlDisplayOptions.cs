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
    public sealed class TemplateListControlDisplayOptions
    {
        public readonly Outputs.TemplateSheetControlInfoIconLabelOptions? InfoIconLabelOptions;
        public readonly Outputs.TemplateListControlSearchOptions? SearchOptions;
        public readonly Outputs.TemplateListControlSelectAllOptions? SelectAllOptions;
        public readonly Outputs.TemplateLabelOptions? TitleOptions;

        [OutputConstructor]
        private TemplateListControlDisplayOptions(
            Outputs.TemplateSheetControlInfoIconLabelOptions? infoIconLabelOptions,

            Outputs.TemplateListControlSearchOptions? searchOptions,

            Outputs.TemplateListControlSelectAllOptions? selectAllOptions,

            Outputs.TemplateLabelOptions? titleOptions)
        {
            InfoIconLabelOptions = infoIconLabelOptions;
            SearchOptions = searchOptions;
            SelectAllOptions = selectAllOptions;
            TitleOptions = titleOptions;
        }
    }
}
