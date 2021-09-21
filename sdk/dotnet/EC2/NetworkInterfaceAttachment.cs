// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    /// <summary>
    /// Resource Type definition for AWS::EC2::NetworkInterfaceAttachment
    /// </summary>
    [Obsolete(@"NetworkInterfaceAttachment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:ec2:NetworkInterfaceAttachment")]
    public partial class NetworkInterfaceAttachment : Pulumi.CustomResource
    {
        [Output("deleteOnTermination")]
        public Output<bool?> DeleteOnTermination { get; private set; } = null!;

        [Output("deviceIndex")]
        public Output<string> DeviceIndex { get; private set; } = null!;

        [Output("instanceId")]
        public Output<string> InstanceId { get; private set; } = null!;

        [Output("networkInterfaceId")]
        public Output<string> NetworkInterfaceId { get; private set; } = null!;


        /// <summary>
        /// Create a NetworkInterfaceAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NetworkInterfaceAttachment(string name, NetworkInterfaceAttachmentArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:NetworkInterfaceAttachment", name, args ?? new NetworkInterfaceAttachmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NetworkInterfaceAttachment(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:NetworkInterfaceAttachment", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing NetworkInterfaceAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NetworkInterfaceAttachment Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new NetworkInterfaceAttachment(name, id, options);
        }
    }

    public sealed class NetworkInterfaceAttachmentArgs : Pulumi.ResourceArgs
    {
        [Input("deleteOnTermination")]
        public Input<bool>? DeleteOnTermination { get; set; }

        [Input("deviceIndex", required: true)]
        public Input<string> DeviceIndex { get; set; } = null!;

        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        [Input("networkInterfaceId", required: true)]
        public Input<string> NetworkInterfaceId { get; set; } = null!;

        public NetworkInterfaceAttachmentArgs()
        {
        }
    }
}
