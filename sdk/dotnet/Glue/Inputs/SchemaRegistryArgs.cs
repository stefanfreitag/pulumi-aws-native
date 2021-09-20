// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue.Inputs
{

    /// <summary>
    /// Identifier for the registry which the schema is part of.
    /// </summary>
    public sealed class SchemaRegistryArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name for the Registry.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Name of the registry in which the schema will be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public SchemaRegistryArgs()
        {
        }
    }
}
