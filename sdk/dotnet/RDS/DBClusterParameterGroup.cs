// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS
{
    /// <summary>
    /// The AWS::RDS::DBClusterParameterGroup resource creates a new Amazon RDS DB cluster parameter group. For more information, see Managing an Amazon Aurora DB Cluster in the Amazon Aurora User Guide.
    /// </summary>
    [AwsNativeResourceType("aws-native:rds:DBClusterParameterGroup")]
    public partial class DBClusterParameterGroup : global::Pulumi.CustomResource
    {
        [Output("dBClusterParameterGroupName")]
        public Output<string> DBClusterParameterGroupName { get; private set; } = null!;

        /// <summary>
        /// A friendly description for this DB cluster parameter group.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.
        /// </summary>
        [Output("family")]
        public Output<string> Family { get; private set; } = null!;

        /// <summary>
        /// An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
        /// </summary>
        [Output("parameters")]
        public Output<object> Parameters { get; private set; } = null!;

        /// <summary>
        /// The list of tags for the cluster parameter group.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DBClusterParameterGroupTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a DBClusterParameterGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DBClusterParameterGroup(string name, DBClusterParameterGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:rds:DBClusterParameterGroup", name, args ?? new DBClusterParameterGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DBClusterParameterGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:rds:DBClusterParameterGroup", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing DBClusterParameterGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DBClusterParameterGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DBClusterParameterGroup(name, id, options);
        }
    }

    public sealed class DBClusterParameterGroupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A friendly description for this DB cluster parameter group.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        /// <summary>
        /// The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.
        /// </summary>
        [Input("family", required: true)]
        public Input<string> Family { get; set; } = null!;

        /// <summary>
        /// An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
        /// </summary>
        [Input("parameters", required: true)]
        public Input<object> Parameters { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.DBClusterParameterGroupTagArgs>? _tags;

        /// <summary>
        /// The list of tags for the cluster parameter group.
        /// </summary>
        public InputList<Inputs.DBClusterParameterGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DBClusterParameterGroupTagArgs>());
            set => _tags = value;
        }

        public DBClusterParameterGroupArgs()
        {
        }
        public static new DBClusterParameterGroupArgs Empty => new DBClusterParameterGroupArgs();
    }
}
