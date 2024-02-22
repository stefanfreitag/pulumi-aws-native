// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight
{
    /// <summary>
    /// Definition of the AWS::QuickSight::Analysis Resource Type.
    /// </summary>
    [AwsNativeResourceType("aws-native:quicksight:Analysis")]
    public partial class Analysis : global::Pulumi.CustomResource
    {
        [Output("analysisId")]
        public Output<string> AnalysisId { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("awsAccountId")]
        public Output<string> AwsAccountId { get; private set; } = null!;

        [Output("createdTime")]
        public Output<string> CreatedTime { get; private set; } = null!;

        [Output("dataSetArns")]
        public Output<ImmutableArray<string>> DataSetArns { get; private set; } = null!;

        [Output("definition")]
        public Output<Outputs.AnalysisDefinition?> Definition { get; private set; } = null!;

        [Output("errors")]
        public Output<ImmutableArray<Outputs.AnalysisError>> Errors { get; private set; } = null!;

        [Output("lastUpdatedTime")]
        public Output<string> LastUpdatedTime { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("parameters")]
        public Output<Outputs.AnalysisParameters?> Parameters { get; private set; } = null!;

        [Output("permissions")]
        public Output<ImmutableArray<Outputs.AnalysisResourcePermission>> Permissions { get; private set; } = null!;

        [Output("sheets")]
        public Output<ImmutableArray<Outputs.AnalysisSheet>> Sheets { get; private set; } = null!;

        [Output("sourceEntity")]
        public Output<Outputs.AnalysisSourceEntity?> SourceEntity { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.QuickSight.AnalysisResourceStatus?> Status { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        [Output("themeArn")]
        public Output<string?> ThemeArn { get; private set; } = null!;

        [Output("validationStrategy")]
        public Output<Outputs.AnalysisValidationStrategy?> ValidationStrategy { get; private set; } = null!;


        /// <summary>
        /// Create a Analysis resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Analysis(string name, AnalysisArgs args, CustomResourceOptions? options = null)
            : base("aws-native:quicksight:Analysis", name, args ?? new AnalysisArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Analysis(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:quicksight:Analysis", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "analysisId",
                    "awsAccountId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Analysis resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Analysis Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Analysis(name, id, options);
        }
    }

    public sealed class AnalysisArgs : global::Pulumi.ResourceArgs
    {
        [Input("analysisId", required: true)]
        public Input<string> AnalysisId { get; set; } = null!;

        [Input("awsAccountId", required: true)]
        public Input<string> AwsAccountId { get; set; } = null!;

        [Input("definition")]
        public Input<Inputs.AnalysisDefinitionArgs>? Definition { get; set; }

        [Input("errors")]
        private InputList<Inputs.AnalysisErrorArgs>? _errors;
        public InputList<Inputs.AnalysisErrorArgs> Errors
        {
            get => _errors ?? (_errors = new InputList<Inputs.AnalysisErrorArgs>());
            set => _errors = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("parameters")]
        public Input<Inputs.AnalysisParametersArgs>? Parameters { get; set; }

        [Input("permissions")]
        private InputList<Inputs.AnalysisResourcePermissionArgs>? _permissions;
        public InputList<Inputs.AnalysisResourcePermissionArgs> Permissions
        {
            get => _permissions ?? (_permissions = new InputList<Inputs.AnalysisResourcePermissionArgs>());
            set => _permissions = value;
        }

        [Input("sheets")]
        private InputList<Inputs.AnalysisSheetArgs>? _sheets;
        public InputList<Inputs.AnalysisSheetArgs> Sheets
        {
            get => _sheets ?? (_sheets = new InputList<Inputs.AnalysisSheetArgs>());
            set => _sheets = value;
        }

        [Input("sourceEntity")]
        public Input<Inputs.AnalysisSourceEntityArgs>? SourceEntity { get; set; }

        [Input("status")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisResourceStatus>? Status { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        [Input("themeArn")]
        public Input<string>? ThemeArn { get; set; }

        [Input("validationStrategy")]
        public Input<Inputs.AnalysisValidationStrategyArgs>? ValidationStrategy { get; set; }

        public AnalysisArgs()
        {
        }
        public static new AnalysisArgs Empty => new AnalysisArgs();
    }
}
