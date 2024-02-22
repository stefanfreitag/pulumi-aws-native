// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise
{
    /// <summary>
    /// Definition of AWS::IoTFleetWise::ModelManifest Resource Type
    /// </summary>
    [Obsolete(@"ModelManifest is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:iotfleetwise:ModelManifest")]
    public partial class ModelManifest : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("lastModificationTime")]
        public Output<string> LastModificationTime { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("nodes")]
        public Output<ImmutableArray<string>> Nodes { get; private set; } = null!;

        [Output("signalCatalogArn")]
        public Output<string> SignalCatalogArn { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.IoTFleetWise.ModelManifestManifestStatus?> Status { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ModelManifest resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ModelManifest(string name, ModelManifestArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iotfleetwise:ModelManifest", name, args ?? new ModelManifestArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ModelManifest(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotfleetwise:ModelManifest", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ModelManifest resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ModelManifest Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ModelManifest(name, id, options);
        }
    }

    public sealed class ModelManifestArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nodes")]
        private InputList<string>? _nodes;
        public InputList<string> Nodes
        {
            get => _nodes ?? (_nodes = new InputList<string>());
            set => _nodes = value;
        }

        [Input("signalCatalogArn", required: true)]
        public Input<string> SignalCatalogArn { get; set; } = null!;

        [Input("status")]
        public Input<Pulumi.AwsNative.IoTFleetWise.ModelManifestManifestStatus>? Status { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public ModelManifestArgs()
        {
        }
        public static new ModelManifestArgs Empty => new ModelManifestArgs();
    }
}
