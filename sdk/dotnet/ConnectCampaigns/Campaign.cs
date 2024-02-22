// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ConnectCampaigns
{
    /// <summary>
    /// Definition of AWS::ConnectCampaigns::Campaign Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:connectcampaigns:Campaign")]
    public partial class Campaign : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Connect Campaign Arn
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Amazon Connect Instance Arn
        /// </summary>
        [Output("connectInstanceArn")]
        public Output<string> ConnectInstanceArn { get; private set; } = null!;

        [Output("dialerConfig")]
        public Output<Outputs.CampaignDialerConfig> DialerConfig { get; private set; } = null!;

        /// <summary>
        /// Amazon Connect Campaign Name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("outboundCallConfig")]
        public Output<Outputs.CampaignOutboundCallConfig> OutboundCallConfig { get; private set; } = null!;

        /// <summary>
        /// One or more tags.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Campaign resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Campaign(string name, CampaignArgs args, CustomResourceOptions? options = null)
            : base("aws-native:connectcampaigns:Campaign", name, args ?? new CampaignArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Campaign(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:connectcampaigns:Campaign", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "connectInstanceArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Campaign resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Campaign Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Campaign(name, id, options);
        }
    }

    public sealed class CampaignArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Connect Instance Arn
        /// </summary>
        [Input("connectInstanceArn", required: true)]
        public Input<string> ConnectInstanceArn { get; set; } = null!;

        [Input("dialerConfig", required: true)]
        public Input<Inputs.CampaignDialerConfigArgs> DialerConfig { get; set; } = null!;

        /// <summary>
        /// Amazon Connect Campaign Name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("outboundCallConfig", required: true)]
        public Input<Inputs.CampaignOutboundCallConfigArgs> OutboundCallConfig { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// One or more tags.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public CampaignArgs()
        {
        }
        public static new CampaignArgs Empty => new CampaignArgs();
    }
}
