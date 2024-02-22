// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    /// <summary>
    /// Resource schema for AWS::SageMaker::Device
    /// </summary>
    [AwsNativeResourceType("aws-native:sagemaker:Device")]
    public partial class Device : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Edge Device you want to register against a device fleet
        /// </summary>
        [Output("device")]
        public Output<Outputs.Device?> DeviceValue { get; private set; } = null!;

        /// <summary>
        /// The name of the edge device fleet
        /// </summary>
        [Output("deviceFleetName")]
        public Output<string> DeviceFleetName { get; private set; } = null!;

        /// <summary>
        /// Associate tags with the resource
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Device resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Device(string name, DeviceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:Device", name, args ?? new DeviceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Device(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:Device", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "device.deviceName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Device resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Device Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Device(name, id, options);
        }
    }

    public sealed class DeviceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Edge Device you want to register against a device fleet
        /// </summary>
        [Input("device")]
        public Input<Inputs.DeviceArgs>? DeviceValue { get; set; }

        /// <summary>
        /// The name of the edge device fleet
        /// </summary>
        [Input("deviceFleetName", required: true)]
        public Input<string> DeviceFleetName { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// Associate tags with the resource
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public DeviceArgs()
        {
        }
        public static new DeviceArgs Empty => new DeviceArgs();
    }
}
