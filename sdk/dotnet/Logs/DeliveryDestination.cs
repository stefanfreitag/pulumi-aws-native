// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Logs
{
    /// <summary>
    /// This structure contains information about one delivery destination in your account.
    /// 
    /// A delivery destination is an AWS resource that represents an AWS service that logs can be sent to CloudWatch Logs, Amazon S3, are supported as Kinesis Data Firehose delivery destinations.
    /// </summary>
    [AwsNativeResourceType("aws-native:logs:DeliveryDestination")]
    public partial class DeliveryDestination : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.
        /// 
        /// The policy must be in JSON string format.
        /// 
        /// Length Constraints: Maximum length of 51200
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Logs::DeliveryDestination` for more information about the expected schema for this property.
        /// </summary>
        [Output("deliveryDestinationPolicy")]
        public Output<object?> DeliveryDestinationPolicy { get; private set; } = null!;

        /// <summary>
        /// Displays whether this delivery destination is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.
        /// </summary>
        [Output("deliveryDestinationType")]
        public Output<string> DeliveryDestinationType { get; private set; } = null!;

        /// <summary>
        /// The ARN of the AWS resource that will receive the logs.
        /// </summary>
        [Output("destinationResourceArn")]
        public Output<string?> DestinationResourceArn { get; private set; } = null!;

        /// <summary>
        /// The name of this delivery destination.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The tags that have been assigned to this delivery destination.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DeliveryDestinationTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a DeliveryDestination resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DeliveryDestination(string name, DeliveryDestinationArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:logs:DeliveryDestination", name, args ?? new DeliveryDestinationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DeliveryDestination(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:logs:DeliveryDestination", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "destinationResourceArn",
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DeliveryDestination resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DeliveryDestination Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DeliveryDestination(name, id, options);
        }
    }

    public sealed class DeliveryDestinationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.
        /// 
        /// The policy must be in JSON string format.
        /// 
        /// Length Constraints: Maximum length of 51200
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Logs::DeliveryDestination` for more information about the expected schema for this property.
        /// </summary>
        [Input("deliveryDestinationPolicy")]
        public Input<object>? DeliveryDestinationPolicy { get; set; }

        /// <summary>
        /// The ARN of the AWS resource that will receive the logs.
        /// </summary>
        [Input("destinationResourceArn")]
        public Input<string>? DestinationResourceArn { get; set; }

        /// <summary>
        /// The name of this delivery destination.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Inputs.DeliveryDestinationTagArgs>? _tags;

        /// <summary>
        /// The tags that have been assigned to this delivery destination.
        /// </summary>
        public InputList<Inputs.DeliveryDestinationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DeliveryDestinationTagArgs>());
            set => _tags = value;
        }

        public DeliveryDestinationArgs()
        {
        }
        public static new DeliveryDestinationArgs Empty => new DeliveryDestinationArgs();
    }
}
