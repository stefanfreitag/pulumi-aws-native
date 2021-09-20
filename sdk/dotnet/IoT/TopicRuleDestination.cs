// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    /// <summary>
    /// Resource Type definition for AWS::IoT::TopicRuleDestination
    /// </summary>
    [AwsNativeResourceType("aws-native:iot:TopicRuleDestination")]
    public partial class TopicRuleDestination : Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN).
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// HTTP URL destination properties.
        /// </summary>
        [Output("httpUrlProperties")]
        public Output<Outputs.TopicRuleDestinationHttpUrlDestinationSummary?> HttpUrlProperties { get; private set; } = null!;

        /// <summary>
        /// The status of the TopicRuleDestination.
        /// </summary>
        [Output("status")]
        public Output<Pulumi.AwsNative.IoT.TopicRuleDestinationTopicRuleDestinationStatus?> Status { get; private set; } = null!;

        /// <summary>
        /// The reasoning for the current status of the TopicRuleDestination.
        /// </summary>
        [Output("statusReason")]
        public Output<string> StatusReason { get; private set; } = null!;

        /// <summary>
        /// VPC destination properties.
        /// </summary>
        [Output("vpcProperties")]
        public Output<Outputs.TopicRuleDestinationVpcDestinationProperties?> VpcProperties { get; private set; } = null!;


        /// <summary>
        /// Create a TopicRuleDestination resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TopicRuleDestination(string name, TopicRuleDestinationArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:iot:TopicRuleDestination", name, args ?? new TopicRuleDestinationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TopicRuleDestination(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iot:TopicRuleDestination", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TopicRuleDestination resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TopicRuleDestination Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new TopicRuleDestination(name, id, options);
        }
    }

    public sealed class TopicRuleDestinationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// HTTP URL destination properties.
        /// </summary>
        [Input("httpUrlProperties")]
        public Input<Inputs.TopicRuleDestinationHttpUrlDestinationSummaryArgs>? HttpUrlProperties { get; set; }

        /// <summary>
        /// The status of the TopicRuleDestination.
        /// </summary>
        [Input("status")]
        public Input<Pulumi.AwsNative.IoT.TopicRuleDestinationTopicRuleDestinationStatus>? Status { get; set; }

        /// <summary>
        /// VPC destination properties.
        /// </summary>
        [Input("vpcProperties")]
        public Input<Inputs.TopicRuleDestinationVpcDestinationPropertiesArgs>? VpcProperties { get; set; }

        public TopicRuleDestinationArgs()
        {
        }
    }
}
