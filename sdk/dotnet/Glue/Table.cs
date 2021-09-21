// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue
{
    /// <summary>
    /// Resource Type definition for AWS::Glue::Table
    /// </summary>
    [Obsolete(@"Table is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:glue:Table")]
    public partial class Table : Pulumi.CustomResource
    {
        [Output("catalogId")]
        public Output<string> CatalogId { get; private set; } = null!;

        [Output("databaseName")]
        public Output<string> DatabaseName { get; private set; } = null!;

        [Output("tableInput")]
        public Output<Outputs.TableTableInput> TableInput { get; private set; } = null!;


        /// <summary>
        /// Create a Table resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Table(string name, TableArgs args, CustomResourceOptions? options = null)
            : base("aws-native:glue:Table", name, args ?? new TableArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Table(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:glue:Table", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Table resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Table Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Table(name, id, options);
        }
    }

    public sealed class TableArgs : Pulumi.ResourceArgs
    {
        [Input("catalogId", required: true)]
        public Input<string> CatalogId { get; set; } = null!;

        [Input("databaseName", required: true)]
        public Input<string> DatabaseName { get; set; } = null!;

        [Input("tableInput", required: true)]
        public Input<Inputs.TableTableInputArgs> TableInput { get; set; } = null!;

        public TableArgs()
        {
        }
    }
}
