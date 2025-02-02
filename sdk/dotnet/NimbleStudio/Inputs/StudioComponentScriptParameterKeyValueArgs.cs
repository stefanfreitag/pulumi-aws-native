// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NimbleStudio.Inputs
{

    /// <summary>
    /// &lt;p&gt;A parameter for a studio component script, in the form of a key:value pair.&lt;/p&gt;
    /// </summary>
    public sealed class StudioComponentScriptParameterKeyValueArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// &lt;p&gt;A script parameter key.&lt;/p&gt;
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// &lt;p&gt;A script parameter value.&lt;/p&gt;
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public StudioComponentScriptParameterKeyValueArgs()
        {
        }
        public static new StudioComponentScriptParameterKeyValueArgs Empty => new StudioComponentScriptParameterKeyValueArgs();
    }
}
