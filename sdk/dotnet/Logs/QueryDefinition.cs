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
    /// The resource schema for AWSLogs QueryDefinition
    /// </summary>
    [AwsNativeResourceType("aws-native:logs:QueryDefinition")]
    public partial class QueryDefinition : Pulumi.CustomResource
    {
        /// <summary>
        /// Optionally define specific log groups as part of your query definition
        /// </summary>
        [Output("logGroupNames")]
        public Output<ImmutableArray<string>> LogGroupNames { get; private set; } = null!;

        /// <summary>
        /// A name for the saved query definition
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Unique identifier of a query definition
        /// </summary>
        [Output("queryDefinitionId")]
        public Output<string> QueryDefinitionId { get; private set; } = null!;

        /// <summary>
        /// The query string to use for this definition
        /// </summary>
        [Output("queryString")]
        public Output<string> QueryString { get; private set; } = null!;


        /// <summary>
        /// Create a QueryDefinition resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public QueryDefinition(string name, QueryDefinitionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:logs:QueryDefinition", name, args ?? new QueryDefinitionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private QueryDefinition(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:logs:QueryDefinition", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing QueryDefinition resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static QueryDefinition Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new QueryDefinition(name, id, options);
        }
    }

    public sealed class QueryDefinitionArgs : Pulumi.ResourceArgs
    {
        [Input("logGroupNames")]
        private InputList<string>? _logGroupNames;

        /// <summary>
        /// Optionally define specific log groups as part of your query definition
        /// </summary>
        public InputList<string> LogGroupNames
        {
            get => _logGroupNames ?? (_logGroupNames = new InputList<string>());
            set => _logGroupNames = value;
        }

        /// <summary>
        /// A name for the saved query definition
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The query string to use for this definition
        /// </summary>
        [Input("queryString", required: true)]
        public Input<string> QueryString { get; set; } = null!;

        public QueryDefinitionArgs()
        {
        }
    }
}
