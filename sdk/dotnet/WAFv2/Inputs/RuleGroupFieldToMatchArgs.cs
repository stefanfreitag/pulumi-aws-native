// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Inputs
{

    /// <summary>
    /// Field of the request to match.
    /// </summary>
    public sealed class RuleGroupFieldToMatchArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// All query arguments of a web request.
        /// </summary>
        [Input("allQueryArguments")]
        public Input<object>? AllQueryArguments { get; set; }

        /// <summary>
        /// The body of a web request. This immediately follows the request headers.
        /// </summary>
        [Input("body")]
        public Input<object>? Body { get; set; }

        [Input("jsonBody")]
        public Input<Inputs.RuleGroupJsonBodyArgs>? JsonBody { get; set; }

        /// <summary>
        /// The HTTP method of a web request. The method indicates the type of operation that the request is asking the origin to perform.
        /// </summary>
        [Input("method")]
        public Input<object>? Method { get; set; }

        /// <summary>
        /// The query string of a web request. This is the part of a URL that appears after a ? character, if any.
        /// </summary>
        [Input("queryString")]
        public Input<object>? QueryString { get; set; }

        [Input("singleHeader")]
        public Input<object>? SingleHeader { get; set; }

        /// <summary>
        /// One query argument in a web request, identified by name, for example UserName or SalesRegion. The name can be up to 30 characters long and isn't case sensitive.
        /// </summary>
        [Input("singleQueryArgument")]
        public Input<object>? SingleQueryArgument { get; set; }

        /// <summary>
        /// The path component of the URI of a web request. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg.
        /// </summary>
        [Input("uriPath")]
        public Input<object>? UriPath { get; set; }

        public RuleGroupFieldToMatchArgs()
        {
        }
    }
}
