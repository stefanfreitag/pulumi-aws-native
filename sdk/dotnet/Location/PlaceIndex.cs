// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Location
{
    /// <summary>
    /// Definition of AWS::Location::PlaceIndex Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:location:PlaceIndex")]
    public partial class PlaceIndex : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        [Output("dataSource")]
        public Output<string> DataSource { get; private set; } = null!;

        [Output("dataSourceConfiguration")]
        public Output<Outputs.PlaceIndexDataSourceConfiguration?> DataSourceConfiguration { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("indexArn")]
        public Output<string> IndexArn { get; private set; } = null!;

        [Output("indexName")]
        public Output<string> IndexName { get; private set; } = null!;

        [Output("pricingPlan")]
        public Output<Pulumi.AwsNative.Location.PlaceIndexPricingPlan?> PricingPlan { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a PlaceIndex resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PlaceIndex(string name, PlaceIndexArgs args, CustomResourceOptions? options = null)
            : base("aws-native:location:PlaceIndex", name, args ?? new PlaceIndexArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PlaceIndex(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:location:PlaceIndex", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "dataSource",
                    "indexName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PlaceIndex resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PlaceIndex Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PlaceIndex(name, id, options);
        }
    }

    public sealed class PlaceIndexArgs : global::Pulumi.ResourceArgs
    {
        [Input("dataSource", required: true)]
        public Input<string> DataSource { get; set; } = null!;

        [Input("dataSourceConfiguration")]
        public Input<Inputs.PlaceIndexDataSourceConfigurationArgs>? DataSourceConfiguration { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("indexName", required: true)]
        public Input<string> IndexName { get; set; } = null!;

        [Input("pricingPlan")]
        public Input<Pulumi.AwsNative.Location.PlaceIndexPricingPlan>? PricingPlan { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public PlaceIndexArgs()
        {
        }
        public static new PlaceIndexArgs Empty => new PlaceIndexArgs();
    }
}
