// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaConvert
{
    /// <summary>
    /// Resource Type definition for AWS::MediaConvert::Preset
    /// </summary>
    [Obsolete(@"Preset is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:mediaconvert:Preset")]
    public partial class Preset : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("category")]
        public Output<string?> Category { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
        /// </summary>
        [Output("settingsJson")]
        public Output<object> SettingsJson { get; private set; } = null!;

        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
        /// </summary>
        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Preset resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Preset(string name, PresetArgs args, CustomResourceOptions? options = null)
            : base("aws-native:mediaconvert:Preset", name, args ?? new PresetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Preset(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:mediaconvert:Preset", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Preset resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Preset Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Preset(name, id, options);
        }
    }

    public sealed class PresetArgs : global::Pulumi.ResourceArgs
    {
        [Input("category")]
        public Input<string>? Category { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
        /// </summary>
        [Input("settingsJson", required: true)]
        public Input<object> SettingsJson { get; set; } = null!;

        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
        /// </summary>
        [Input("tags")]
        public Input<object>? Tags { get; set; }

        public PresetArgs()
        {
        }
        public static new PresetArgs Empty => new PresetArgs();
    }
}
