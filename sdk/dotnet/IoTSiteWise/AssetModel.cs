// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTSiteWise
{
    /// <summary>
    /// Resource schema for AWS::IoTSiteWise::AssetModel
    /// </summary>
    [AwsNativeResourceType("aws-native:iotsitewise:AssetModel")]
    public partial class AssetModel : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the asset model, which has the following format.
        /// </summary>
        [Output("assetModelArn")]
        public Output<string> AssetModelArn { get; private set; } = null!;

        /// <summary>
        /// The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.
        /// </summary>
        [Output("assetModelCompositeModels")]
        public Output<ImmutableArray<Outputs.AssetModelCompositeModel>> AssetModelCompositeModels { get; private set; } = null!;

        /// <summary>
        /// A description for the asset model.
        /// </summary>
        [Output("assetModelDescription")]
        public Output<string?> AssetModelDescription { get; private set; } = null!;

        /// <summary>
        /// The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.
        /// </summary>
        [Output("assetModelHierarchies")]
        public Output<ImmutableArray<Outputs.AssetModelHierarchy>> AssetModelHierarchies { get; private set; } = null!;

        /// <summary>
        /// The ID of the asset model.
        /// </summary>
        [Output("assetModelId")]
        public Output<string> AssetModelId { get; private set; } = null!;

        /// <summary>
        /// A unique, friendly name for the asset model.
        /// </summary>
        [Output("assetModelName")]
        public Output<string> AssetModelName { get; private set; } = null!;

        /// <summary>
        /// The property definitions of the asset model. You can specify up to 200 properties per asset model.
        /// </summary>
        [Output("assetModelProperties")]
        public Output<ImmutableArray<Outputs.AssetModelProperty>> AssetModelProperties { get; private set; } = null!;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the asset model.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.AssetModelTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a AssetModel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AssetModel(string name, AssetModelArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:iotsitewise:AssetModel", name, args ?? new AssetModelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AssetModel(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotsitewise:AssetModel", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing AssetModel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AssetModel Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AssetModel(name, id, options);
        }
    }

    public sealed class AssetModelArgs : global::Pulumi.ResourceArgs
    {
        [Input("assetModelCompositeModels")]
        private InputList<Inputs.AssetModelCompositeModelArgs>? _assetModelCompositeModels;

        /// <summary>
        /// The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.
        /// </summary>
        public InputList<Inputs.AssetModelCompositeModelArgs> AssetModelCompositeModels
        {
            get => _assetModelCompositeModels ?? (_assetModelCompositeModels = new InputList<Inputs.AssetModelCompositeModelArgs>());
            set => _assetModelCompositeModels = value;
        }

        /// <summary>
        /// A description for the asset model.
        /// </summary>
        [Input("assetModelDescription")]
        public Input<string>? AssetModelDescription { get; set; }

        [Input("assetModelHierarchies")]
        private InputList<Inputs.AssetModelHierarchyArgs>? _assetModelHierarchies;

        /// <summary>
        /// The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.
        /// </summary>
        public InputList<Inputs.AssetModelHierarchyArgs> AssetModelHierarchies
        {
            get => _assetModelHierarchies ?? (_assetModelHierarchies = new InputList<Inputs.AssetModelHierarchyArgs>());
            set => _assetModelHierarchies = value;
        }

        /// <summary>
        /// A unique, friendly name for the asset model.
        /// </summary>
        [Input("assetModelName")]
        public Input<string>? AssetModelName { get; set; }

        [Input("assetModelProperties")]
        private InputList<Inputs.AssetModelPropertyArgs>? _assetModelProperties;

        /// <summary>
        /// The property definitions of the asset model. You can specify up to 200 properties per asset model.
        /// </summary>
        public InputList<Inputs.AssetModelPropertyArgs> AssetModelProperties
        {
            get => _assetModelProperties ?? (_assetModelProperties = new InputList<Inputs.AssetModelPropertyArgs>());
            set => _assetModelProperties = value;
        }

        [Input("tags")]
        private InputList<Inputs.AssetModelTagArgs>? _tags;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the asset model.
        /// </summary>
        public InputList<Inputs.AssetModelTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.AssetModelTagArgs>());
            set => _tags = value;
        }

        public AssetModelArgs()
        {
        }
        public static new AssetModelArgs Empty => new AssetModelArgs();
    }
}
