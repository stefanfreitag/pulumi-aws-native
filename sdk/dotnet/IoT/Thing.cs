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
    /// Resource Type definition for AWS::IoT::Thing
    /// </summary>
    [Obsolete(@"Thing is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:iot:Thing")]
    public partial class Thing : Pulumi.CustomResource
    {
        [Output("attributePayload")]
        public Output<Outputs.ThingAttributePayload?> AttributePayload { get; private set; } = null!;

        [Output("thingName")]
        public Output<string?> ThingName { get; private set; } = null!;


        /// <summary>
        /// Create a Thing resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Thing(string name, ThingArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:iot:Thing", name, args ?? new ThingArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Thing(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iot:Thing", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Thing resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Thing Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Thing(name, id, options);
        }
    }

    public sealed class ThingArgs : Pulumi.ResourceArgs
    {
        [Input("attributePayload")]
        public Input<Inputs.ThingAttributePayloadArgs>? AttributePayload { get; set; }

        [Input("thingName")]
        public Input<string>? ThingName { get; set; }

        public ThingArgs()
        {
        }
    }
}
