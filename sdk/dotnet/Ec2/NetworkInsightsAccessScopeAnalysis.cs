// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    /// <summary>
    /// Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:NetworkInsightsAccessScopeAnalysis")]
    public partial class NetworkInsightsAccessScopeAnalysis : global::Pulumi.CustomResource
    {
        [Output("analyzedEniCount")]
        public Output<int> AnalyzedEniCount { get; private set; } = null!;

        [Output("endDate")]
        public Output<string> EndDate { get; private set; } = null!;

        [Output("findingsFound")]
        public Output<Pulumi.AwsNative.Ec2.NetworkInsightsAccessScopeAnalysisFindingsFound> FindingsFound { get; private set; } = null!;

        [Output("networkInsightsAccessScopeAnalysisArn")]
        public Output<string> NetworkInsightsAccessScopeAnalysisArn { get; private set; } = null!;

        [Output("networkInsightsAccessScopeAnalysisId")]
        public Output<string> NetworkInsightsAccessScopeAnalysisId { get; private set; } = null!;

        [Output("networkInsightsAccessScopeId")]
        public Output<string> NetworkInsightsAccessScopeId { get; private set; } = null!;

        [Output("startDate")]
        public Output<string> StartDate { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.Ec2.NetworkInsightsAccessScopeAnalysisStatus> Status { get; private set; } = null!;

        [Output("statusMessage")]
        public Output<string> StatusMessage { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a NetworkInsightsAccessScopeAnalysis resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NetworkInsightsAccessScopeAnalysis(string name, NetworkInsightsAccessScopeAnalysisArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:NetworkInsightsAccessScopeAnalysis", name, args ?? new NetworkInsightsAccessScopeAnalysisArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NetworkInsightsAccessScopeAnalysis(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:NetworkInsightsAccessScopeAnalysis", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "networkInsightsAccessScopeId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing NetworkInsightsAccessScopeAnalysis resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NetworkInsightsAccessScopeAnalysis Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new NetworkInsightsAccessScopeAnalysis(name, id, options);
        }
    }

    public sealed class NetworkInsightsAccessScopeAnalysisArgs : global::Pulumi.ResourceArgs
    {
        [Input("networkInsightsAccessScopeId", required: true)]
        public Input<string> NetworkInsightsAccessScopeId { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public NetworkInsightsAccessScopeAnalysisArgs()
        {
        }
        public static new NetworkInsightsAccessScopeAnalysisArgs Empty => new NetworkInsightsAccessScopeAnalysisArgs();
    }
}
