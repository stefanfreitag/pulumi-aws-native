// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTEvents
{
    /// <summary>
    /// The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.
    /// </summary>
    [AwsNativeResourceType("aws-native:iotevents:Input")]
    public partial class Input : global::Pulumi.CustomResource
    {
        [Output("inputDefinition")]
        public Output<Outputs.InputDefinition> InputDefinition { get; private set; } = null!;

        /// <summary>
        /// A brief description of the input.
        /// </summary>
        [Output("inputDescription")]
        public Output<string?> InputDescription { get; private set; } = null!;

        /// <summary>
        /// The name of the input.
        /// </summary>
        [Output("inputName")]
        public Output<string?> InputName { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// 
        /// For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.InputTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Input resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Input(string name, InputArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iotevents:Input", name, args ?? new InputArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Input(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotevents:Input", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Input resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Input Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Input(name, id, options);
        }
    }

    public sealed class InputArgs : global::Pulumi.ResourceArgs
    {
        [Input("inputDefinition", required: true)]
        public Input<Inputs.InputDefinitionArgs> InputDefinition { get; set; } = null!;

        /// <summary>
        /// A brief description of the input.
        /// </summary>
        [Input("inputDescription")]
        public Input<string>? InputDescription { get; set; }

        /// <summary>
        /// The name of the input.
        /// </summary>
        [Input("inputName")]
        public Input<string>? InputName { get; set; }

        [Input("tags")]
        private InputList<Inputs.InputTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// 
        /// For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        /// </summary>
        public InputList<Inputs.InputTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.InputTagArgs>());
            set => _tags = value;
        }

        public InputArgs()
        {
        }
        public static new InputArgs Empty => new InputArgs();
    }
}
